from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
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

    # Define the paths of JavaScript files to be used ti render the page.
    scripts = [
        'http://d3v7w7xrm71xax.cloudfront.net/jquery-3.5.1.min.js',
        'http://d3v7w7xrm71xax.cloudfront.net/resize-sensor-1.2.2.js',
    ]

    # Handle GET requests.
    def get(self, request):
        # TODO Description
        check_cached_repos()

        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': self.page_title,
            'scripts': self.scripts,
            'projects': Project.objects.all(),
            'repos': get_repos()
        }

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)


# A view class which displays a single project that is specified in a GET request by its ID.
class ProjectView(View):
    # Define the path of the view's HTML template.
    template_name = 'projects/project/page.html'

    # Handle GET requests.
    def get(self, request, project_id=None):
        # Try to get a project with the requested project ID from the database, or raise a Http404 exception if one does
        # not exist.
        project = get_object_or_404(Project, id=project_id)

        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': project.title,
            'project': project,
        }

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)
