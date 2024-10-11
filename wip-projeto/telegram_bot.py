import telebot
import os
from dotenv import load_dotenv
from entidades.mensagem_telegram import Mensagem
from database.insert_mensage import cadastrar_mensagem_database

# importa o TOKEN do Telegram
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# instancia o Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# salvar mensagem no Banco de Dados (mySQL):
def salvar_mensagem_BD(mensagem):
    msg = Mensagem(mensagem.id, mensagem.from_user.id, mensagem.from_user.first_name, mensagem.from_user.last_name, mensagem.date, mensagem.json['text'])
    cadastrar_mensagem_database(msg.message_id, msg.user_id, msg.first_name, msg.last_name, msg.timestamp, msg.text_msg)    

# Mensagem handler    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    salvar_mensagem_BD(mensagem)
    bot.send_message(mensagem.chat.id, "mensagem recebida, estaremos analisando.")

bot.polling()