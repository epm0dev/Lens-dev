import os
from django.core.wsgi import get_wsgi_application


# Set the default settings module for the django wsgi application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lens.settings')

# Get the wsgi application.
application = get_wsgi_application()
