import os
from django.core.asgi import get_asgi_application


# Set the default settings module for the django asgi application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lens.settings')

# Get the asgi application.
application = get_asgi_application()
