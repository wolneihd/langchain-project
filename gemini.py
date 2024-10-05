from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# pip install langchain-google-genai

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
)

messages = """
considerando o feedback abaixo, diga se foi: positivo, neutro ou negativo.

O serviço prestado pelo colaborador Wesley é horrível. Fiquei 20min aguardando, sem nenhum aviso que iria atrasar.

resposta deve ser um SQL query:
- resposta01: positivo, neutro ou negativo.
- resposta02: resumo em até 5 palavras.

INSERT INTO feedbacks (resposta) VALUES ("resposta01","resposta02");
"""

ai_msg = llm.invoke(messages)

print(ai_msg)