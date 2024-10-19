import LLM0
import LLM1
import db


con=db.create_connection("localhost", "root", "", "schoola")
info=db.get_tables_and_columns(con, "schoola")
def chat(Question):
    response_0=str(LLM0.chat_SQL(Question, info))#get the sql querry needed
    querry = extract_query_from_string(response_0).replace('"', "'").strip()  # Replace double quotes with single quotes
    print(repr(querry))  # Check the cleaned query

    querry_result=db.execute_query(con, querry)#excute the querry
    response_1=str(LLM1.chat(Question,querry_result))#get the response from the pyschologist
    return response_1


def extract_query_from_string(response):
    response=response.split("Result")
    response=response[1].split(":")
    response=response[1].split("}")
    response=response[0]
    response=response.replace("'","")
    return response

#Example usage:
# print(chat("what you think about John in general ?"))