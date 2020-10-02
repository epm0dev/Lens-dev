from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.mail import send_mail
from django.contrib import messages


# A view class which displays my contact information and a form to contact me directly.
class ContactView(View):
    # Define the path of the view's HTML template.
    template_name = 'contact/contact.html'

    # Define the title of the view's page.
    page_title = 'Contact'

    # Handle GET requests.
    def get(self, request):
        # Create a context dictionary to populate the view's HTML template with.
        context = {'page_title': self.page_title}

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)

    # Handle POST requests.
    @staticmethod
    def post(request):
        # TODO Documentation
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        minitial = request.POST.get('middle-initial')
        email = request.POST.get('email-address')
        phone = request.POST.get('phone-number')
        message = request.POST.get('message')
        if minitial:
            name = f'{first_name} {minitial}. {last_name}'
        else:
            name = f'{first_name} {last_name}'
        if phone:
            message_header = f'{name}\n{email}\n{phone}\n'
        else:
            message_header = f'{name}\n{email}\n'
        status = send_mail(
            f'{name} has contacted you',
            f'{message_header}\nMessage Body:\n{message}',
            'New Message From Lens <contact@epm0dev.me>',
            ['epmancin@ncsu.edu'],
        )

        if status:
            messages.info(request, 'Contact form submitted successfully!')
            return redirect('/contact/')
        else:
            messages.info(request, 'There was an error submitting your message. Please try again in awhile.')
            return redirect('/contact/')
