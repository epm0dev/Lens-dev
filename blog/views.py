from django.shortcuts import render
from django.views.generic.base import View


# A view class which contains a personal blog.
class BlogHomeView(View):
    # Define the path of the view's HTML template.
    template_name = 'blog/home.html'

    # Define the title of the view's page.
    page_title = 'Blog'

    # Handle GET requests.
    def get(self, request):
        # Create a context dictionary to populate the view's HTML template with.
        context = {'page_title': self.page_title}

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)
