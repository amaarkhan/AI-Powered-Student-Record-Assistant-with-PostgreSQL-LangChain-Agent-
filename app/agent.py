from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_agent():
    db_uri = os.getenv("DB_URI")
    db = SQLDatabase.from_uri(db_uri)

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0
    )

    agent = create_sql_agent(
        llm=llm,
        toolkit=SQLDatabaseToolkit(db=db, llm=llm),
        verbose=True
    )

    return agent
