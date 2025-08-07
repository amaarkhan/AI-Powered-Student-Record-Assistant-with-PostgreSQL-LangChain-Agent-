# 🎓 AI-Powered Student Record Assistant  
_Query your PostgreSQL database using natural language with Google Gemini 1.5 Flash + LangChain_

---

## 📌 Overview
This project is an AI-powered agent that connects to a PostgreSQL database and allows you to ask questions in plain English (or other languages).  
The agent translates your query into SQL, executes it, and returns the results — powered by **LangChain** and **Gemini 1.5 Flash**.

---

## 🚀 Features
- **Natural language to SQL** queries
- **Gemini 1.5 Flash LLM** integration
- **PostgreSQL database** backend
- Modular Python code structure
- Easily customizable schema
- Extensible to web apps (e.g., Streamlit, Flask)

---

## 🛠️ Tech Stack
- **Python** 3.10+
- **PostgreSQL**
- **LangChain** (latest v0.2+ style)
- **Google Generative AI API** (`gemini-1.5-flash`)
- **SQLAlchemy** + `psycopg2`

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ai-student-record-assistant.git
cd ai-student-record-assistant
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Install & Set Up PostgreSQL
Download from https://www.postgresql.org/download/

During installation, set:

Username: postgres (or your custom username)

Password: remember this!

Port: 5432

Add PostgreSQL to PATH if not already.

🗄️ Database Setup
Create the database
bash
Copy
Edit
psql -U postgres
CREATE DATABASE student_db;
\c student_db
Create the table
sql
Copy
Edit
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    gpa NUMERIC,
    year TEXT
);
Insert sample data
sql
Copy
Edit
INSERT INTO students (name, age, department, gpa, year) VALUES
('Amaar Khan', 20, 'CS', 3.9, 'Sophomore'),
('Ali Raza', 22, 'SE', 3.6, 'Senior'),
('Sara Imran', 19, 'IT', 2.9, 'Freshman');
🔑 Environment Variables
Create a .env file in the root folder:

env
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key
DB_URI=postgresql+psycopg2://postgres:yourpassword@localhost:5432/student_db
Get your Google API Key from:
👉 https://makersuite.google.com/app/apikey

▶️ Running the Project
bash
Copy
Edit
python main.py
Example interaction:

yaml
Copy
Edit
Ask your DB: those students whose gpa is greater than 3.5
Agent Answer:
Amaar Khan, Ali Raza
📂 Project Structure
bash
Copy
Edit
.
├── app/
│   ├── agent.py             # LLM + SQL Agent setup
│   ├── query_interface.py   # Simple interface to query the DB
├── main.py                  # Entry point
├── requirements.txt
├── .env                     # Environment variables (not in git)
└── README.md
🛠️ How It Works
User enters a natural language query

LangChain SQL Agent parses the intent

Agent:

Fetches database schema

Generates SQL query using Gemini 1.5 Flash

Executes the query in PostgreSQL

Returns results in plain language

🧩 Possible Extensions
Add a Streamlit UI for a chat interface

Connect to multiple databases

Integrate data visualization for numeric queries

Add authentication to protect DB access

Deploy to a web server or cloud function

⚠️ Notes
Use LangChain v0.2+ imports to avoid deprecation warnings

Keep .env file out of version control (.gitignore)

Ensure PostgreSQL service is running before starting the app

