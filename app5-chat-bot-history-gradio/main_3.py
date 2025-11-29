# Added History My Way
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  # Import message classes for chat history

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = """
You are Einstein.
Answer questions through Einstein's questioning and reasoning...
Answer in 2-6 sentences.
You should have a sense of humor.
"""

# Initialize chat history list with system message (sent once at start)
history = [SystemMessage(content=system_prompt)]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":  # Use .lower() for case-insensitive exit
        break

    # Add current user input to history as HumanMessage
    history.append(HumanMessage(content=user_input))

    # Invoke model with FULL history (not just current input)
    response = llm.invoke(history)

    # Add model's response to history as AIMessage for next turn
    history.append(AIMessage(content=response.content))

    print("Einstein:", response.content)  # Added "Einstein:" prefix for clarity
