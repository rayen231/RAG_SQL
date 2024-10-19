from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
import agent

app = FastAPI()
# Define a model for the request body
class QuestionRequest(BaseModel):
    question: str


@app.post("/get-query/")
async def get_query(request: QuestionRequest):
    # Process the incoming question
    print(request)
    response = agent.chat(request.question)

    # Convert response data to JSON string
    json_response = json.dumps(response, indent=4)

    # Return JSON response as a downloadable file
    return JSONResponse(content=response)