# text-to-sql
A simple, end-to-end demo that converts natural language into SQL queries using LLMs (Deepseek R1 8B via Ollama) and executes them on a sample SQLite Bookstore database, all through an interactive Streamlit interface.


## Project Overview

Modern data systems are full of valuable insights, but querying databases still requires technical knowledge of **SQL**.  
This project bridges that gap by allowing **ANYONE** (even non-technical users) to interact with structured data using **PLAIN ENGLISH**.

The core idea is simple but powerful:
### “Turn natural language into SQL.”

Using **Large Language Models (LLMs)** through **Ollama** and **LangChain**, this project translates user questions into executable SQL queries that run against a real **SQLite database**.

---

### What It Does:
- Converts **natural language questions** (like “Show all customers from Austin”) into **SQL queries**.
- Executes those SQL queries safely on a local **Bookstore database**.
- Displays the results instantly in a clean **Streamlit** web interface.
- Provides a transparent, explainable way to explore relational data without knowing SQL syntax.

---

### How It Works:
1. **User Input:** The user types a question into the Streamlit interface.  
2. **Schema Extraction:** The app uses **SQLAlchemy** to read the database’s schema (tables, columns, and relationships).  
3. **LLM Conversion:** The schema and user question are passed to the **Deepseek R1 8B** model via **LangChain** and **Ollama**.  
4. **SQL Generation:** The model returns a syntactically valid SQL query based on the schema.  
5. **Query Execution:** The SQL is executed on a **local SQLite database**, and results are fetched.  
6. **Result Display:** The data is displayed in the Streamlit frontend in real-time.

### You can type queries like:

> “Show all customers from Austin”  
> “What is the total revenue from all orders?”  
> “List products in the Fiction category costing more than 15 dollars”

and the system will:
1. Generate an SQL query using the Deepseek model.
2. Execute it on a local SQLite database.
3. Display the results in an elegant Streamlit app.

---

### Example in Action:

**User Query:**  
> “Show me all Fiction books priced above 15 dollars.”

**Generated SQL:**  
```sql
SELECT name, price FROM products WHERE category = 'Fiction' AND price > 15;
```
## Project Structure
```
📂 text-to-sql-deepseek
├── Database.py                   # Creates and populates the sample SQLite database
├── App.py                        # Core logic: schema extraction, LLM prompt, SQL execution
├── frontend.py                   # Streamlit interface for user interaction
├── requirements.txt              # Dependency list
└── README.md                     # Project documentation
```

## Requirements
### Create a virtual environment using uv:
```
uv init .
``` 

### Install the required dependencies:

```bash
uv pip install -r requirements.txt

requirements.txt
streamlit
langchain
langchain_community
langchain_ollama
langchain_core
sqlalchemy

```
## Ollama Setup

This project uses **Ollama**. To run the Deepseek model locally:

1. Download and install Ollama
2. Pull the Deepseek model
> ollama pull deepseek-r1:8b
3. Verify it’s running
> ollama list
