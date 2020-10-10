from django.shortcuts import render
from django.views.generic.base import View


# A view class which displays the contents of my resume with formatting that matches the rest of the website.
class ResumeView(View):
    # Define the path of the view's HTML template.
    template_name = 'resume/resume.html'

    # Define the title of the view's page.
    page_title = 'Resume'

    # Define the path from which to download the resume page's stylesheet.
    stylesheet = 'http://d3v7w7xrm71xax.cloudfront.net/resume.min.css'

    # Define the path from which to download the resume.
    download_path = 'http://d3v7w7xrm71xax.cloudfront.net/Ethan_Mancini_Resume.pdf'

    # Handle GET requests.
    def get(self, request):
        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': self.page_title,
            'stylesheet': self.stylesheet,
            'download_path': self.download_path
        }

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)
