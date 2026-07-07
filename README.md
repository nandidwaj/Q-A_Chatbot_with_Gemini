# Enhanced Q&A Chatbot with Gemini

A simple interactive Q&A chatbot built using Streamlit, LangChain, and Google Gemini models. The application allows users to select a Gemini model, configure response settings, enter their Gemini API key, and ask questions through a web-based interface.

The project also integrates LangSmith tracing for monitoring and debugging LangChain executions.

## Features

- Interactive chatbot interface using Streamlit
- Integration with Google Gemini models
- LangChain-based prompt and response pipeline
- Multiple Gemini model selection
- Adjustable temperature
- Adjustable maximum token limit
- Secure API key input through the Streamlit sidebar
- Environment variable management using `python-dotenv`
- LangSmith tracing and project monitoring
- String output parsing using `StrOutputParser`

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- LangSmith
- python-dotenv

## Project Structure

```text
Q&A-CHATBOT/
│
├── venv/
│
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
