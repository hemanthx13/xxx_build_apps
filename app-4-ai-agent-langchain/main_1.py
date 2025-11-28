from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = "You are a helpful assistant. You will help the user add tasks"
user_input = "How many legs Cow has?"

prompt = ChatPromptTemplate ([
    ("system", system_prompt),
    ("user", user_input)
])

chain = prompt | llm | StrOutputParser()

#print(chain)
'''
first=ChatPromptTemplate(input_variables=[], input_types={}, partial_variables={}, messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='You are a helpful assistant. You will help the user add tasks'), additional_kwargs={}), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='What day is it today?'), additional_kwargs={})]) middle=[ChatGoogleGenerativeAI(model='models/gemini-2.5-flash', google_api_key=SecretStr('**********'), temperature=0.3, client=<google.ai.generativelanguage_v1beta.services.generative_service.client.GenerativeServiceClient object at 0x00000190B4DB7050>, default_metadata=(), model_kwargs={})] last=StrOutputParser()
'''
response = chain.invoke({"input":user_input})

print(response)