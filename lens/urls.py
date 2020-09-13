"""Lens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from .views import AboutView

import resume.urls
import projects.urls
import contact.urls
import blog.urls


# Define the URL patterns for the main application.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='about/')),
    re_path(r'about/?', AboutView.as_view()),
    re_path(r'resume/?', include(resume.urls)),
    re_path(r'projects/?', include(projects.urls)),
    re_path(r'blog/?', include(blog.urls)),
    re_path(r'contact/?', include(contact.urls)),
]
