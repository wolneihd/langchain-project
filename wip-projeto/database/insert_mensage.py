import mysql.connector;
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acesse as variáveis usando os.environ
db_user = os.getenv('BD_USER')
db_password = os.getenv('BD_PASSWORD')
db_port = os.getenv('BD_PORT')
db_host = os.getenv('BD_HOST')
db_database = os.getenv('BD_DATABASE')

# configurações do BD como um dicionário
config = {
    'host': db_host,
    'port': db_port,
    'user': db_user,
    'password': db_password,
    'database': db_database
}

# cria conexão com o DB
def conectar():
    conexao = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database
    )
    print("conectado com sucesso!")
    return conexao

# insere mensagem no DB
def cadastrar_mensagem_database(message_id:int, user_id:int, first_name:str, last_name:str, timestamp:int, text_msg:str):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO mensagens (message_id, user_id, first_name, last_name, timestamp_cod, text_msg) VALUES (%s, %s, %s, %s, %s, %s);", (message_id, user_id, first_name, last_name, timestamp, text_msg))
        conexao.commit() 
        print(f"Cadastrado com sucesso: \nid: {message_id} \nuser_id: {user_id} \nfirst_name: {first_name} \nlast_name: {last_name} \ntimestamp: {timestamp} \ntexto: {text_msg}")
    except Exception as e:
        print("Erro ao salvar no DB:", e)  # Imprime a exceção
    finally:     
        conexao.close()
