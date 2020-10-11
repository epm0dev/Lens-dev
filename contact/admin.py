from django.contrib import admin
from django_ses.views import dashboard


# Register the django-ses dashboard with the admin site so that SES stats can be viewed.
admin.site.register_view('django-ses', dashboard, 'Django SES Stats')
