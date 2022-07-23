"""
ASGI config for kevin_webserver project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

# channel model
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# asgi model
from django.core.asgi import get_asgi_application

from kevin_webserver.routing import web_socket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kevin_webserver.settings')  # default

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    "websocket": AuthMiddlewareStack(
        URLRouter(
            web_socket_urlpatterns
        )
    ),
})
