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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from .views import HomeView
from adminplus.sites import AdminSitePlus

import resume.urls
import projects.urls
import contact.urls
import blog.urls


# TODO Documentation
admin.site = AdminSitePlus()
admin.autodiscover()

# Define the URL patterns for the main application.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    re_path(r'^resume/?', include(resume.urls)),
    re_path(r'^projects/?', include(projects.urls)),
    # re_path(r'^blog/?', include(blog.urls)),
    re_path(r'^contact/?', include(contact.urls)),
]

# TODO Documentation
urlpatterns += (url(r'^admin/django-ses/', include('django_ses.urls')),)
