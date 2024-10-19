import os
from crewai import Agent, Task, Crew, Process
import db
def config():
    os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
    os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'  # Adjust based on available model
    os.environ["OPENAI_API_KEY"] = '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'
    # email="congrat mr rayen the application for job is approved!!! "
    GROQ_API_KEY = ""

def chat(Question,info):
    config()
    document_assistant = Agent(
        role="Pyschologist and sentiment Assistant",
        goal="You will assit the user in understanding the sentiment and the psychology State of the user he asked about",
        backstory="You are an expert Pyschologist and sentiment Assistant. Given an input question and information about the user , you will give a detailed analysis.",
        verbose=True,
        allow_delegation=False
    )
    
    document_task = Task(
        description=f"""
        Given this question : {Question}, create a detailed analysis of the user That we have those info about him: {info}""",
        agent=document_assistant,
        expected_output="{Question:'the question , 'Result':'The analysis' :"
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
# info= "[(1, 'John', 'Doe', 'Happy', 'Struggles to engage but makes efforts', 'Rarely, seems uninterested', 'Verbally, with ease', 'Attentive and focused throughout')]"
# result = chat("How is jhon doing ?",info)
# print(result)