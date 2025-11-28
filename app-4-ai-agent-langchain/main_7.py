# Adding User Input with while loop & Chat History

from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic_core.core_schema import model_field
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from todoist_api_python.api import TodoistAPI


load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todoist_api_key)

@tool
def add_task(task, des=None):
    """Add a new task to the user's task list. Use this when the user wants to add or create a task"""
    todoist.add_task(content=task, description=des)

tools = [add_task]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = "You are a helpful assistant. You will help the user add tasks & Answer Questions"


prompt = ChatPromptTemplate ([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

history = []
while True:
    user_input = input("Add your Task (type 'stop' to quit): ")
    if user_input.lower() == "stop":
        break
    response = agent_executor.invoke({"input":user_input, "history":history})
    print(response['output'])
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response['output']))