# blog/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/blog/', consumers.BlogConsumer.as_asgi()),
]