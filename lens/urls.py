from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from .views import HomeView
from adminplus.sites import AdminSitePlus

import resume.urls
import projects.urls
import contact.urls
# import blog.urls


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
