from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from user.models import UserModel
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        # self.room_name = "test_comsumer"
        # self.room_group_name = "test_consumer_group"
        # async_to_sync(self.channel_layer.group_add)(self.room_name, self.room_group_name)
        # self.accept(
        #     self.send(text_data = json.dumps({'status': 'connected from django channel'}))
        # )
        async_to_sync(self.channel_layer.group_add)(str(self.scope['user'].id), self.channel_name)
        self.accept()

    def receive(self, text_data):
        print(text_data)
        receiver = json.loads(text_data)['receiver']
        data = json.loads(text_data)['message']

        self.send(text_data= json.dumps({'status': 'we got you'}))
        
        obj = self.create_message(receiver, data, type)


    def disconnect(self,*args, **kwargs):
        print("disconnect")


    def send_notification(self, event):
        print(event)
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))
        print("send notification")

"""
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
"""