from django.shortcuts import render
from django.views.generic.base import View


# A view class which displays a simple welcome page with my basic information.
class HomeView(View):
    # Define the path of the view's HTML template.
    template_name = 'lens/home.html'

    # Define the title of the view's page.
    page_title = 'Home'

    # Handle GET requests.
    def get(self, request):
        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': self.page_title
        }

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)
