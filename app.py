# Extract Schema
from sqlalchemy import create_engine, inspect
import json
import re
import sqlite3

db_url = "sqlite:///bookstore.db"

# Extract the database schema
def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}

    # Get table names and their columns
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [col['name'] for col in columns]

    return json.dumps(schema)


# Text to SQL (Deepseek with Ollama)
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Convert text prompt to SQL query
def text_to_sql(schema, prompt):
    SYSTEM_PROMPT = """
        You are an expert SQL generator. Given a database schema and a user prompt, generate a valid SQL query that answers the prompt. 
        Only use the tables and columns provided in the schema. ALWAYS ensure the SQL syntax is correct and avoid using any unsupported features. 
        Output only the SQL as your response will be directly used to query data from the database. No preamble please. Do not use <think> tags.
    """

    # Create prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Schema:\n{schema}\n\nUser Prompt:\n{user_prompt}\n\nSQL Query:")
    ])

    # Initialize Ollama LLM with Deepseek model
    model = OllamaLLM(model= "deepseek-r1:8b")

    # Create the chain
    chain = prompt_template | model

    # Invoke the chain with schema and user prompt
    raw_response = chain.invoke({"schema": schema, "user_prompt": prompt})
    cleaned_response = re.sub(r"<think>.*?<\/think>", "", raw_response, flags=re.DOTALL)
    return cleaned_response.strip()

# Get data from database based on user prompt
def get_data_from_database(prompt):
    schema = extract_schema(db_url)
    sql_query = text_to_sql(schema, prompt)
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    results = res.fetchall()
    conn.close()
    return results