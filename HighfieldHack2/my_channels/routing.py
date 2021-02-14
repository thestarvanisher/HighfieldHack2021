# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('debates/', consumers.DebateConsumer.as_asgi()),
    re_path('view/', consumers.ArgumentConsumer.as_asgi()),
]