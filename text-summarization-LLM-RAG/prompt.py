import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


API_KEY = ''
os.environ["OPENAI_API_KEY"] = API_KEY

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

answer_prompt = PromptTemplate.from_template(
    """Based on the user's question, the SQL query, and the SQL result, answer the user's question.

Question: {question}
SQL Query: {query}
SQL Resul: {result}
Answer: """
)