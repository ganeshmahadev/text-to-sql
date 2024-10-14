from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load gemini model and provide SQL query as response
def get_gemini_pro(question, prompt):
    # Convert prompt list to a single string
    prompt_str = ''.join(prompt)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt_str + question)
    return response.text

# Function to retrieve the query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    curr = conn.cursor()
    curr.execute(sql)
    rows = curr.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the SQL code should not have ``` in beginning or end and sql word in output.
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    # Get the generated SQL query
    response = get_gemini_pro(question, prompt)
    
    # Display the SQL query in the Streamlit app
    st.subheader("Generated SQL Query:")
    st.code(response, language="sql")
    
    # Execute the SQL query and show the results
    response = read_sql_query(response, "student.db")
    
    st.subheader("Query Results:")
    for row in response:
        st.write(row)
