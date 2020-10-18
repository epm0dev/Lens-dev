from django.urls import re_path
from .views import ProjectHomeView


# Define the URL patterns for the projects application.
urlpatterns = [
    re_path(r'^$', ProjectHomeView.as_view()),
]
