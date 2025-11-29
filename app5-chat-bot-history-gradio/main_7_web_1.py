from dotenv import load_dotenv
import os
import gradio as gr

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3,
)

system_prompt = """
You are Einstein.
Answer questions through Einstein's questioning and reasoning...
You will speak from your point of view. You will share personal things from your life 
even when the user don't ask for it. For example, if the user asks about the theory of 
relativity, you will share your personal experiences with it and not only explain the theory.
Answer in 1-2 sentences.
You should have a sense of humor.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

chain = prompt | llm | StrOutputParser()

def chat(user_input, hist):
    # hist is a list of {"role": "...", "content": "..."} dicts (type='messages')
    print(user_input, hist)

    langchain_history = []
    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))

    response = chain.invoke({"input": user_input, "history": langchain_history})

    # Return empty textbox value and updated messages list
    return "", hist + [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": response},
    ]

def clear_chat():
    return "", []

page = gr.Blocks(
    title="Chat with Einstein",
    #theme=gr.themes.Soft()
)

with page:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to your personal conversation with Albert.
        """
    )

    # IMPORTANT: type='messages' so hist matches what ChatInterface docs describe [web:24]
    chatbot = gr.Chatbot(avatar_images=['user.png', 'einstein.png'], height=450)
    msg = gr.Textbox(placeholder="Ask Einstein anything…", show_label=False)

    # Press Enter to send, just like in the screenshot
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])

page.launch(share=True, server_port=7860, show_error=True, theme=gr.themes.Soft())
