from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login as channel_login
from .services import login
from django.contrib.auth.models import AnonymousUser
from user_auth_management.models import User


class LoginWebConsumer(AsyncWebsocketConsumer):

    def receive(self, text_data):
        email = text_data.get('email')
        password = text_data.get('password')
        token, user = login(email, password)
        await channel_login(self.scope, user)
        await database_sync_to_async(self.scope["session"].save)()
        self.send({
            'refresh': str(token),
            'access': str(token.access_token),
            'userId': str(user.id)
        })
