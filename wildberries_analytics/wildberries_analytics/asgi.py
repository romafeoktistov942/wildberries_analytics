import os
from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "wildberries_analytics.settings"
)

application = get_asgi_application()
