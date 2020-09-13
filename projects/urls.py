from django.urls import re_path
from .views import ProjectHomeView, ProjectView


# Define the URL patterns for the projects application.
urlpatterns = [
    re_path(r'^$', ProjectHomeView.as_view()),
    re_path(r'(?P<project_id>\w{1,50})/?$', ProjectView.as_view()),
]
