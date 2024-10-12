from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from database.comandos_db import buscar_todas_mensagens

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # consultar todas as mensagens
    @app.route('/', methods=['GET'])
    def obter_todas_as_mensagens():
        lista_usuarios = buscar_todas_mensagens()
        lista_usuarios_dict = [usuario.to_dict() for usuario in lista_usuarios]
        return jsonify(lista_usuarios_dict)
    
    app.run(port=5000,host='localhost',debug=True)

if __name__ == "__main__":
    # monta a API
    montar_API()