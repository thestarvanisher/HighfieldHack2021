"""
ASGI config for HighfieldHack2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# HighfieldHack2/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import HighfieldHack2.my_channels.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HighfieldHack2.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            HighfieldHack2.my_channels.routing.websocket_urlpatterns
        )
    ),
})