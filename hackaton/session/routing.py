from django.urls import re_path

from session.consumer import LiveScoreConsumer

websocket_urlpatterns = [
    re_path('ws/socket-server/', LiveScoreConsumer.as_asgi())
]
