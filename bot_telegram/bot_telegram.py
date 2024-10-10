from flask import Flask, request
import requests

import os
from dotenv import load_dotenv

# sugestão código:
# https://github.com/dehatanes/telegram-bots-boilerplates/tree/main

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Recebe os dados enviados pelo Telegram
        data = request.json
        print(f"Mensagem recebida: {data}")

        # Pega o chat ID e o texto da mensagem
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']

        # Exemplo de envio de resposta
        send_message(chat_id, f"Você disse: {message_text}")

        return "OK", 200
    return "Método não suportado", 400

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(port=5000)
