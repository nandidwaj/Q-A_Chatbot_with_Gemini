import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

##Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with Gemini"

##Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    client = genai.Client(api_key=api_key)
    llm = ChatGoogleGenerativeAI(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})
    return answer

## Title of the app
st.title("Enhanced Q&A Chatbot with Gemini")

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your API Key:",type="password")

## Drop down to select various models

llm = st.sidebar.selectbox("Select an model",["gemini-3.5-flash","gemini-3.1-flash-lite","gemini-3.1-pro-preview"])

# Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)


## Main interface for user input 
st.write("Go ahead and ask any question")
user_input = st.text_input("You: ")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Provide the query")