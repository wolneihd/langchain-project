import threading
from flask import Flask, jsonify
from flask_cors import CORS  # Importar CORS
import telebot
import os
from dotenv import load_dotenv
from database.comandos_db import buscar_todas_mensagens, cadastrar_mensagem_database
from entidades.mensagem_telegram import Mensagem

# Carregar variáveis de ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Defina o caminho da pasta onde as imagens serão salvas
IMAGE_SAVE_PATH = 'images/'

# Certifique-se de que a pasta existe
if not os.path.exists(IMAGE_SAVE_PATH):
    os.makedirs(IMAGE_SAVE_PATH)

# Criar uma instância do bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Função para o bot do Telegram
def start_bot():
    def salvar_mensagem_BD(mensagem):
        msg = Mensagem(
            mensagem.id,
            mensagem.from_user.id,
            mensagem.from_user.first_name,
            mensagem.from_user.last_name,
            mensagem.date,
            mensagem.json['text']
        )
        cadastrar_mensagem_database(msg.message_id, msg.user_id, msg.first_name, msg.last_name, msg.timestamp, msg.text_msg)    

    @bot.message_handler(func=lambda mensagem: True)
    def responder(mensagem):
        salvar_mensagem_BD(mensagem)
        bot.send_message(mensagem.chat.id, "mensagem recebida, estaremos analisando.")

    # Função para tratar mensagens de foto
    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        try:
            print(message) #'content_type': 'photo'
            # implementar: 1. insere no DB: model, DB, comando_db >> remodelar Db
            # ORDER BY user_id (pensar em como agregar as respostas)

            # Pega o arquivo de maior resolução da foto
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            # Nomeia o arquivo com o ID da mensagem
            file_name = f"{message.message_id}.jpg"
            file_path = os.path.join(IMAGE_SAVE_PATH, file_name)

            # Salva o arquivo na pasta designada
            with open(file_path, 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, f"Imagem salva na pasta como: {file_name}!")
        except Exception as e:
            bot.reply_to(message, f"Erro ao salvar a imagem: {e}")

    bot.polling()

# Configuração da API Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as rotas

@app.route('/')
def obter_todas_as_mensagens():
    listaMensagens = buscar_todas_mensagens()
    return jsonify([mensagem.to_dict() for mensagem in listaMensagens])

# Função para iniciar a API Flask
def start_api():
    app.run(port=5000, host='localhost')  # Remover debug=True

if __name__ == "__main__":
    # Criar threads para o bot e a API
    bot_thread = threading.Thread(target=start_bot)
    api_thread = threading.Thread(target=start_api)

    # Iniciar as threads
    bot_thread.start()
    api_thread.start()

    # Aguardar que ambas as threads terminem (se necessário)
    bot_thread.join()
    api_thread.join()
