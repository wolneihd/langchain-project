import telebot
import os
from dotenv import load_dotenv
from entidades.mensagem_telegram import Mensagem
from database.comandos_db import cadastrar_mensagem_database

# importa o TOKEN do Telegram
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# instancia o Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# salvar mensagem no Banco de Dados (mySQL):
def salvar_mensagem_BD(mensagem):
    msg = Mensagem(mensagem.id, mensagem.from_user.id, mensagem.from_user.first_name, mensagem.from_user.last_name, mensagem.date, mensagem.json['text'])
    cadastrar_mensagem_database(msg.message_id, msg.user_id, msg.first_name, msg.last_name, msg.timestamp, msg.text_msg)    

# Defina o caminho da pasta onde as imagens serão salvas
IMAGE_SAVE_PATH = 'images/'

# Certifique-se de que a pasta existe
if not os.path.exists(IMAGE_SAVE_PATH):
    os.makedirs(IMAGE_SAVE_PATH)

# Mensagem handler    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    salvar_mensagem_BD(mensagem)
    bot.send_message(mensagem.chat.id, "mensagem recebida, estaremos analisando.")

# Função para tratar mensagens de foto
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        print(message) #'content_type': 'photo'
        # implementar: 1. insere no DB - 2. como apresentar do Front?

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