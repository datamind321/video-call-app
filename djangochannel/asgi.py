"""
ASGI config for djangochannel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path 
from chat.consumers import VideoChat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochannel.settings')

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        URLRouter([
            path('ws/',VideoChat.as_asgi())
        ])
    )
})