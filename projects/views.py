from django.shortcuts import render
from django.views.generic.base import View
from lens.tasks import check_cached_repos, get_repos
from .models import Project


# A view class which displays a list of project cards for each of the projects in the database.
class ProjectHomeView(View):
    # Define the path of the view's HTML template.
    template_name = 'projects/home.html'

    # Define the title of the view's page.
    page_title = 'Projects'

    # Define the URL from which the projects page's stylesheet is served.
    stylesheet = 'http://d3v7w7xrm71xax.cloudfront.net/projects.min.css'

    # Define the paths of JavaScript files to be used to render the page.
    scripts = [
        'http://d3v7w7xrm71xax.cloudfront.net/jquery-3.5.1.min.js',
        'http://d3v7w7xrm71xax.cloudfront.net/resize-sensor-1.2.2.js',
        'http://d3v7w7xrm71xax.cloudfront.net/projects.min.js'
    ]

    # Handle GET requests.
    def get(self, request):
        # Spin off a django background task to check whether or not the cached version of the github repository needs to
        # be updated, and to do so if necessary.
        check_cached_repos()

        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': self.page_title,
            'stylesheet': self.stylesheet,
            'scripts': self.scripts,
            'projects': Project.objects.all(),
            'repos': get_repos()
        }

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)
