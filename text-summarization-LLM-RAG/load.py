import pandas as pd
from db_config import db_connection
import time


    
    
def load_data1(data, host, user, pwd, db, tbl):
    # Define the insert queries
    insrt_query = f"""INSERT INTO {tbl} 
        (category, vendors, page_content) 
        VALUES (%s, %s, %s)"""


    conn, cursor = db_connection(host, user, pwd, db)   
    start_time = time.time()  # Start the timer
    

    columns = ['category', 'vendors', 'page_content']

    # Convert the DataFrame to a list of tuples for batch insertion
    rows = [tuple(data[col].iloc[i] for col in columns) for i in range(len(data))]
    # Execute batch insertion
    cursor.executemany(insrt_query, rows)
    
    elapsed_time = (time.time() - start_time) * 1000  # Calculate the elapsed time
    
    # Commit the changes to the database and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"Data loaded successfully in {elapsed_time:.2f} ms.")
    
    
def load_data2(data, host, user, pwd, db, tbl):
    # Define the insert queries
    insrt_query = f"""INSERT INTO {tbl} 
        (category, vendors, label,page_content) 
        VALUES (%s, %s, %s,%s)"""


    conn, cursor = db_connection(host, user, pwd, db)   
    start_time = time.time()  # Start the timer
    

    columns = ['category', 'vendors','Label','cleaned_text']

    # Convert the DataFrame to a list of tuples for batch insertion
    rows = [tuple(data[col].iloc[i] for col in columns) for i in range(len(data))]
    # Execute batch insertion
    cursor.executemany(insrt_query, rows)
    
    elapsed_time = (time.time() - start_time) * 1000  # Calculate the elapsed time
    
    # Commit the changes to the database and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"Data loaded successfully in {elapsed_time:.2f} ms.")