import json
from channels.generic.websocket import WebsocketConsumer

class DebateConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        did = text_data_json['id']
        title = text_data_json['title']
        desc = text_data_json['description']

        self.send(text_data=json.dumps({
            'id': did,
            'title': title,
            'description': desc
        }))