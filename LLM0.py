import os
from crewai import Agent, Task, Crew, Process
import db
def config():
    os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
    os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'  # Adjust based on available model
    os.environ["OPENAI_API_KEY"] = 'api key'  # Add your API key here
    # email="congrat mr rayen the application for job is approved!!! "
    GROQ_API_KEY = ""

def chat_SQL(Question,db_info):
    config()
    document_assistant = Agent(
        role="SQLite expert",
        goal="You will Transform a question given into a correct MySQL query ",
        backstory="You are a SQLite expert. Given an input question, first create a syntactically correct Mysql query to run, than check if the query is correct and return the result in a jason format.",
        verbose=True,
        allow_delegation=False
    )
    
    document_task = Task(
        description=f"""
        Given this question : {Question}, create ONLY a syntactically correct Mysql query to run knowing that our data base looks like this : {db_info}, than check if the query is correct and dont return anything expect than the querry and dont forget the '; 'in the end of querry ! """,
        agent=document_assistant,
        expected_output="{'Result':'The Querry'}"
    )
    
    crew = Crew(
        agents=[document_assistant],
        tasks=[document_task],
        verbose=1,
        process=Process.sequential,
        Output_Log_File=True
    )
    
    output = crew.kickoff()
    
    return output

#Example usage:
# con=db.create_connection("localhost", "root", "", "schoola")
# print(con)
# info=db.get_tables_and_columns(con, "schoola")
# result = chat_SQL("what you think about jhon in general ?",info)
# print(result)
