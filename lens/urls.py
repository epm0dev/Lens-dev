from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from .views import HomeView
from adminplus.sites import AdminSitePlus
import resume.urls
import projects.urls
import contact.urls
# import blog.urls


# Swap out the default admin site for an adminplus admin site instance.
admin.site = AdminSitePlus()

# Autodiscover admin models.
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

# Add a URL pattern to allow access to the django-ses admin page.
urlpatterns += (url(r'^admin/django-ses/', include('django_ses.urls')),)
