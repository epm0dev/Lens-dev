from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from django.http import HttpResponse
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

    # Define the URL from which the contact page's stylesheet is served.
    stylesheet = 'http://d3v7w7xrm71xax.cloudfront.net/contact.min.css'

    # Define a list of URL's from which the contact page's JavaScript files are served.
    scripts = [
        'http://d3v7w7xrm71xax.cloudfront.net/jquery-3.5.1.min.js',
        'http://d3v7w7xrm71xax.cloudfront.net/contact.min.js'
    ]

    # Handle GET requests.
    def get(self, request):
        # Create a context dictionary to populate the view's HTML template with.
        context = {
            'page_title': self.page_title,
            'stylesheet': self.stylesheet,
            'scripts': self.scripts
        }

        # Return the view's template, rendered with the information in the context dictionary.
        return render(request, self.template_name, context)

    # Handle POST requests.
    @staticmethod
    def post(request):
        try:
            # Get form data from the request.
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            minitial = request.POST.get('middle-initial')
            email = request.POST.get('email-address')
            phone = request.POST.get('phone-number')
            message = request.POST.get('message')
        except KeyError:
            # If a KeyError is raised, the post request did not contain the proper fields.
            return HttpResponse(status=400, reason='Malformed POST request')

        # Check if any required fields are empty.
        if not all([first_name, last_name, email, message]):
            # If a required field is empty, return a response with HTTP status code 400.
            return HttpResponse(status=400, reason='One or more required fields was left empty')

        try:
            # Try to validate the email address.
            validate_email(email)
        except ValidationError:
            # If a ValidationError is raised, return a response with HTTP status code 400.
            return HttpResponse(status=400, reason='Invalid email address')

        # Create a new regex validator instance to check for valid phone numbers.
        validate_phone = RegexValidator(regex='^[1-9][0-9]{2}-[0-9]{3}-[0-9]{4}$')

        try:
            # Try to validate the phone number.
            validate_phone(phone)
        except ValidationError:
            # If a ValidationError is raised, return a response with HTTP status code 400.
            return HttpResponse(status=400, reason='Invalid phone number')

        # Build a string containing the full name of the person who sent the message.
        if minitial:
            name = f'{first_name} {minitial}. {last_name}'
        else:
            name = f'{first_name} {last_name}'

        # Build a string containing a header block to display before the contents of the message in the email.
        if phone:
            message_header = f'{name}\n{email}\n{phone}\n'
        else:
            message_header = f'{name}\n{email}\n'

        # Send an email to my personal email containing the information submitted by the user and store the status code
        # that is returned.
        status = send_mail(
            f'{name} has contacted you',  # The email's subject
            f'{message_header}\nMessage Body:\n{message}',  # The email's body
            'Lens Messaging Service <contact@epm0dev.me>',  # The from email, with a decorative name
            ['epmancin@ncsu.edu'],  # The email to send the email to
        )

        # Add an appropriate message, based on the status code, with the django.contrib.messages api.
        if status:
            messages.info(request, 'Contact form submitted successfully!')
        else:
            messages.info(request, 'There was an error submitting your message. Please try again in awhile.')

        # Redirect the user back to the contact page.
        return redirect('/contact/')
