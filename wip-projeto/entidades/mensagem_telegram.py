class Mensagem():
    def __init__(self, message_id:int, user_id:int, first_name:str, last_name:str, timestamp:int, text_msg:str):
        self.message_id = message_id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.timestamp = timestamp
        self.text_msg = text_msg