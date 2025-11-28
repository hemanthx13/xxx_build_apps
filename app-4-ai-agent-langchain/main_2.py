from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic_core.core_schema import model_field
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

@tool
def add_task():
    """Add a new task to the user's task list. Use this when the user wants to add or create a task"""
    print('Adding a task')
    print("Task added")

tools = [add_task]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = "You are a helpful assistant. You will help the user add tasks"

## See how two different inputs execute tools via the agents

user_input = "Add a new task to buy milk?"
##  Below `add_task` was executed from tool, also note {} as it executed with any inputs as we have not defined them
'''
> Entering new AgentExecutor chain...

Invoking: `add_task` with `{}`


Adding a task
Task added
NoneI have added a new task to buy milk.

> Finished chain.
{'input': 'Add a new task to buy milk?', 'output': 'I have added a new task to buy milk.'}
'''

#user_input = "How many legs Cow has?"
##  Below no tool was executed
'''
> Entering new AgentExecutor chain...
A cow has 4 legs.

> Finished chain.
{'input': 'How many legs Cow has?', 'output': 'A cow has 4 legs.'}
'''
prompt = ChatPromptTemplate ([
    ("system", system_prompt),
    ("user", user_input),
    MessagesPlaceholder("agent_scratchpad")
])

#chain = prompt | llm | StrOutputParser()

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

#response = chain.invoke({"input":user_input})

response = agent_executor.invoke({"input":user_input})

print(response)