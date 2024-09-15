# blog/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BlogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('1------------')
        await self.accept()

    async def disconnect(self, close_code):
        print('2------------')
        pass

    async def receive(self, text_data):
        print('3------------')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))