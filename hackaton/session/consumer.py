import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class LiveScoreConsumer(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()
