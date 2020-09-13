from django.urls import path
from .views import BlogHomeView


# Define the URL patterns for the contact application.
urlpatterns = [
    path('', BlogHomeView.as_view()),
]
