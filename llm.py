import streamlit as st
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = AzureChatOpenAI()

# Create the Embedding model
from langchain_openai import AzureOpenAIEmbeddings

embeddings = AzureOpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY_EMBEDDING"),
                                               azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_EMBEDDING"))

