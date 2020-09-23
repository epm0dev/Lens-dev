from django.urls import path, re_path
from .views import ContactView


# Define the URL patterns for the contact application.
urlpatterns = [
    path('', ContactView.as_view()),
    re_path(r'submit/?', ContactView.as_view()),
]
