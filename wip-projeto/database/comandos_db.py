import mysql.connector;
from dotenv import load_dotenv
import os
from entidades.mensagem_telegram import TipoMensagem, Mensagem, Usuario
from typing import List

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

def buscar_todas_mensagens():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT 
        usuarios.id, 
        usuarios.user_id,
        usuarios.first_name,
        usuarios.last_name,
        mensagens.id,
        mensagens.id_tipo_mensagem, 
        mensagens.usuarios_id,
        mensagens.timestamp_cod,
        mensagens.text_msg,
        tiposmensagem.id,
        tiposmensagem.tipo
    FROM usuarios
        INNER JOIN mensagens ON usuarios.id = mensagens.usuarios_id
        INNER JOIN tiposmensagem ON tiposmensagem.id = mensagens.id_tipo_mensagem;
    """)
    
    registros = cursor.fetchall()
    conexao.close()
    
    # Dicionário para armazenar usuários e suas mensagens
    usuarios_dict = {}

    for registro in registros:
        usuario_id = registro[0]
        
        # Verifica se o usuário já foi instanciado
        if usuario_id not in usuarios_dict:
            # Instancia o usuário (registro[0] a [3])
            usuario = Usuario(
                id=registro[0],
                user_id=registro[1],
                first_name=registro[2],
                last_name=registro[3]
            )
            usuarios_dict[usuario_id] = usuario
        
        # Instancia o TipoMensagem (registro[9] e [10])
        tipo_mensagem = TipoMensagem(registro[9], registro[10])

        # Instancia a Mensagem (registro[4] a [8], além de tipo_mensagem)
        mensagem = Mensagem(
            id_usuario=registro[6],
            timestamp=registro[7],
            text_msg=registro[8],
            tipoMensagem=tipo_mensagem
        )

        # Adiciona a mensagem ao usuário correspondente
        usuarios_dict[usuario_id].mensagens.append(mensagem)

    # Retorna os objetos de usuários com suas respectivas mensagens
    return list(usuarios_dict.values())

def salvar_registro(user_id:int, first_name:str, last_name:str, timestamp_cod:int, text_msg:str, tipo:str):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE user_id = %s;",(user_id,))
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            cursor.execute("INSERT INTO usuarios (user_id, first_name, last_name) VALUES (%s, %s, %s);", (user_id, first_name, last_name))
            conexao.commit() 
        cursor.execute("SELECT id FROM usuarios WHERE user_id = %s;",(user_id,))
        id_usuario = cursor.fetchall()
        id_usuario = id_usuario[0][0]
        if (tipo == "texto"):
            cursor.execute("INSERT INTO mensagens (id_tipo_mensagem, usuarios_id, timestamp_cod, text_msg) VALUES (%s, %s, %s, %s);", (1, id_usuario, timestamp_cod, text_msg))
        conexao.commit()
        print("salvo com sucesso!")
    except Exception as e:
        print("Erro ao salvar no DB:", e)  # Imprime a exceção
    finally:     
        conexao.close()    
