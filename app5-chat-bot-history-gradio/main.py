from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3
)

response = llm.invoke([{"role":"user", "content":"How many legs tiger has?"}])
print(response)
'''
content='A tiger has **4** legs.' additional_kwargs={} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'model_name': 'gemini-2.5-flash', 'safety_ratings': [], 'model_provider': 'google_genai'} id='lc_run--e58c0329-45d5-43c1-a006-7f7b250d263f-0' usage_metadata={'input_tokens': 7, 'output_tokens': 81, 'total_tokens': 88, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 73}}

'''
print(type(response))
print(response.content)
print(response.response_metadata['model_provider'])
print(response.response_metadata['model_name'])
print(response.usage_metadata)
