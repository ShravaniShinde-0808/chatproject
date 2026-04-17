"""
ASGI config for chatproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

# ⚠️ STEP 1: settings set कर (FIRST)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

# ⚠️ STEP 2: django setup
import django
django.setup()

# ⚠️ STEP 3: बाकी imports
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat import routing

# ⚠️ STEP 4: application define
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})