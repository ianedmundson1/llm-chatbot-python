import streamlit as st
from langchain_openai import AzureChatOpenAI
llm = AzureChatOpenAI()

# Create the Embedding model
from langchain_openai import AzureOpenAIEmbeddings

embeddings = AzureOpenAIEmbeddings()