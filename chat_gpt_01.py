from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()
OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = OPEN_AI_KEY

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
messages = [
    ("system", "Você é um assistente útil que traduz inglês para francês."),
    ("human", "I love programming.")
]
response = llm.invoke(messages)
print(response.content)