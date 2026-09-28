import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Uses Meta's Llama 3 model completely for free
model = ChatGroq(model="llama-3.3-70b-specdec") 

response = model.invoke("Write a haiku about programming.")
print(response.content)
