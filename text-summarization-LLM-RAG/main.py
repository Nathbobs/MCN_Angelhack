from tbl_sql import TABLE_SQL
from db_config import setup_table
from config import TABLE1,TABLE2, USER_NAME,PASSWORD,DATABASE_NAME, HOST_NAME
from load import load_data1, load_data2
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain 
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from prompt import llm, answer_prompt


def readFile(path):
    return pd.read_csv(path)

data= readFile("data/electronics_dummy.csv")
summary_vendors_labels =readFile("data/vendors_metric_rev.csv")
data_for_review =readFile("data/dataset_with_sentiment.csv")

data_for_el = data_for_review.loc[data_for_review["category"]=="Electronics_5"].reset_index(drop=True)

data_for_el = data_for_el[['category', 'vendors','Label', 'cleaned_text']]

# Group by vendors and label, and then summarize the cleaned_text for each group
summary_df = data_for_el.groupby(['vendors', 'Label'])['cleaned_text'].apply(lambda texts: ' '.join(texts)).reset_index()
labels = set(summary_df.Label)

s2_uri = f"singlestoredb://{USER_NAME}:{PASSWORD}@{HOST_NAME}:3306/{DATABASE_NAME}"




if __name__ == "__main__":
    import time
    summary_review = []
    avg_summ=[]
    
    engine = create_engine(s2_uri)
    db_conn = SQLDatabase(engine)
    vendors = set(data.vendors) #get the unique vendors

    # Create a tool to execute queries on the database
    execute_query = QuerySQLDataBaseTool(db=db_conn)
   

    # Create an SQL query chain using the language model and database
    write_query = create_sql_query_chain(llm, db_conn)
    
    
    answer = answer_prompt | llm | StrOutputParser()

    # Define the full chain of operations
    chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        )
        | answer
    )

    # load to database
    for i in [TABLE1, TABLE2]:
        if i == TABLE1:
            setup_table(TABLE_SQL[i], HOST_NAME, USER_NAME, PASSWORD, DATABASE_NAME)
            load_data1(data, HOST_NAME, USER_NAME, PASSWORD, DATABASE_NAME, i)
    
    
            for i in vendors:
                
                # Invoke the chain with a user question
                start_time = time.time()
                response = chain.invoke({"question": f"can you give a short but consise summary about the page content related to {i}?"})
                elapsed_time = (time.time() - start_time) * 1000
                print(f"Execution time for getting the question embedding: {elapsed_time:.2f} milliseconds")
                summary_review.append(response)
                
            data["summary"] = response
            
            data[["category","vendors","summary"]].to_csv("rst_data/data_summarization.csv", index=False)
            
        else:
            setup_table(TABLE_SQL[i], HOST_NAME, USER_NAME, PASSWORD, DATABASE_NAME) #send to database
            load_data2(summary_df, HOST_NAME, USER_NAME, PASSWORD, DATABASE_NAME, i)
            
            for i in vendors:
                for e in labels:
                    
                    # Invoke the chain with a user question
                    start_time = time.time()
                    response = chain.invoke({"question": f"can you give a short but consise summary about the page content related to {i} and where label is {e}?"})
                    elapsed_time = (time.time() - start_time) * 1000
                    print(f"Execution time for getting the question embedding: {elapsed_time:.2f} milliseconds")
                    avg_summ.append(response)
                
            summary_df["summary"] = avg_summ
            
            summary_df[["vendors","Label","review"]].to_csv("rst_data/rev_good_bad_avg.csv", index=False)