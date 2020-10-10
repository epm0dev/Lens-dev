from django.urls import path
from .views import ResumeView


# Define the URL patterns for the resume application.
urlpatterns = [
    path('', ResumeView.as_view()),
]
