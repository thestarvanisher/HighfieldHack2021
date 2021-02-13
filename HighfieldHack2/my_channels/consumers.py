import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class DebateConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name+"_senddebate"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

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

    def sendDebate(self, event):
        print("###Event triggered###")
        self.send(text_data=json.dumps({
            'id': event['id'],
            'title': event['title'],
            'description': event['desc']
        }))