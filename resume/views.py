from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import mimetypes
from django.conf.urls.static import static


# A view class which displays the contents of my resume with formatting that matches the rest of the website.
class ResumeView(View):
    # Define the path of the view's HTML template.
    template_name = 'resume/resume.html'

    # Define the title of the view's page.
    page_title = 'Resume'

    # Handle GET requests.
    def get(self, request):
        # Create a context dictionary to populate the view's HTML template with.
        context = {'page_title': self.page_title}

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)


# TODO Documentation
def download_resume(request, file):
    file_path = '../static/other/resume.pdf'
    filename = 'resume.pdf'

    file = open(file_path, 'r')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
