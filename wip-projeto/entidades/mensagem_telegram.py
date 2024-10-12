class TipoMensagem:
    def __init__(self, id_tipo, descricao):
        self.id_tipo = id_tipo
        self.descricao = descricao

    def to_dict(self):
        return {
            "id_tipo": self.id_tipo,
            "descricao": self.descricao
        }


class Mensagem:
    def __init__(self, id_usuario, timestamp, text_msg, tipoMensagem):
        self.id_usuario = id_usuario
        self.timestamp = timestamp
        self.text_msg = text_msg
        self.tipoMensagem = tipoMensagem

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "timestamp": self.timestamp,
            "text_msg": self.text_msg,
            "tipoMensagem": self.tipoMensagem.to_dict()
        }


class Usuario:
    def __init__(self, id, user_id, first_name, last_name):
        self.id = id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.mensagens = []

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mensagens": [mensagem.to_dict() for mensagem in self.mensagens]
        }
