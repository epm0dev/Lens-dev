from django.urls import path
from .views import ResumeView  # , download_resume


# Define the URL patterns for the resume application.
urlpatterns = [
    path('', ResumeView.as_view()),
    # path('<str:file>/', download_resume),
]
