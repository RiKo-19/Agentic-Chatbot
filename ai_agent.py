# Setup API keys for Groq, OpenAI, and Tavily

import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE")

# Setup LLMs & Tools

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

openai_llm = ChatOpenAI(model = "gpt-4o-mini",
                        api_key=OPENROUTER_API_KEY,
                        base_url=OPENAI_API_BASE)

groq_llm = ChatGroq(model = "llama-3.3-70b-versatile")

search_tool=TavilySearch(max_results=2)

# Setup AI Agent with tools

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI Chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, 
                         api_key=OPENROUTER_API_KEY,
                         base_url=OPENAI_API_BASE
                         )

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent=create_react_agent(
        model=llm,
        tools=tools,
        prompt = system_prompt
    )

    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_message[-1]  # Print the last AI message in the response
