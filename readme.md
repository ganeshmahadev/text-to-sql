# Gemini SQL Query Generator and Executor

This project is a web-based application that generates SQL queries based on natural language questions. The app leverages Google Generative AI's Gemini model to convert English questions into SQL queries and then executes those queries against an SQLite database to retrieve results. The app is built with Streamlit for an interactive user interface.

## Features

- Converts natural language questions into SQL queries using the Gemini model from Google Generative AI.
- Displays the generated SQL query in the web app.
- Executes the SQL query on an SQLite database.
- Displays the results of the executed query in the web app.

## Prerequisites

Before running the application, make sure you have the following installed on your system:

- Python 3.7 or above
- SQLite (for managing the database)
- [Google Generative AI API](https://developers.generativeai.google) key

## Installation

### 1. Clone the Repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies. 
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows

### 3. Install Requirements
pip install -r requirements.txt

### 4. Setup Environment variables
GOOGLE_API_KEY=your_google_api_key_here
Make sure you replace your_google_api_key_here with your actual API key.

### 5. Run the streamlit app
streamlit run app.py

