# Setup Pydantic model

from pydantic import BaseModel
from typing import List

class Requeststate(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Setup AI Agent from Frontend Request

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "llama-3.3-70b-versatile", "google/gemini-2.0-flash-lite-001", "gpt-4o-mini"]

app = FastAPI(title="Agentic Chatbot")

@app.post("/chat")
def chat(request: Requeststate):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Model name is invalid. Please choose a different model."}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    #create AI Agent and get response from it
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response
    
# Run app & Explore Swagger UI Docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)