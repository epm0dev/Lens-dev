from django.urls import path
from .views import ContactView


# Define the URL patterns for the contact application.
urlpatterns = [
    path('', ContactView.as_view()),
]
