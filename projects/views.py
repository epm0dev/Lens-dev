from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from lens.tasks import check_cached_repos
from .models import Project


# A view class which displays a list of project cards for each of the projects in the database.
class ProjectHomeView(View):
    # Define the path of the view's HTML template.
    template_name = 'projects/home.html'

    # Define the title of the view's page.
    page_title = 'Projects'

    # Handle GET requests.
    def get(self, request):
        # TODO Description
        check_cached_repos()

        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': self.page_title,
            # TODO Sort projects here. (Completed -> In Progress -> Paused -> Future)
            'projects': Project.objects.all(),
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
