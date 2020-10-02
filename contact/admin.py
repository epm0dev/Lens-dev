from django.contrib import admin
from django_ses.views import dashboard


# TODO Documentation
admin.site.register_view('django-ses', dashboard, 'Django SES Stats')
