import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class DebateConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name + "_senddebate"
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
            'subtype': event['subtype'],
            'id': event['id'],
            'title': event['title'],
            'description': event['desc']
        }))


class ArgumentConsumer(WebsocketConsumer):
    def connect(self):
        print("###Connect###")
        self.room_name = 'event'
        self.room_group_name = self.room_name + "_sendarg"
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
        atype = text_data_json['type']
        aid = text_data_json['id']
        title = text_data_json['title']
        desc = text_data_json['description']

        self.send(text_data=json.dumps({
            'type': atype,
            'id': aid,
            'title': title,
            'description': desc
        }))

    def sendArg(self, event):
        print("###Argument event triggered###")
        self.send(text_data=json.dumps({
            'is_for': event['is_for'],
            'id': event['id'],
            'title': event['title'],
            'description': event['desc']
        }))

class PollConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name + "_sendchoice"
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
        name = text_data_json['poll']
        title = text_data_json['title']

        self.send(text_data=json.dumps({
            "poll": name,
            "title": title
        }))

    def sendChoice(self, event):
        self.send(text_data=json.dumps({
            'poll': event['poll'],
            'id': event['id'],
            'title': event['title']
        }))

class VoteConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name + "_sendvote"
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
        name = text_data_json['poll']
        title = text_data_json['title']
        choice = text_data_json['choice']

        self.send(text_data=json.dumps({
            "poll": name,
            "choice": choice
        }))

    def sendChoice(self, event):
        self.send(text_data=json.dumps({
            'poll': event['poll'],
            "choice": event["choice"]
        }))