from django.core import mail
from django.test import TestCase, SimpleTestCase, Client


# A test case for the home page.
class HomePageTestCase(SimpleTestCase):
    # Set up the class for testing.
    @classmethod
    def setUpClass(cls):
        # Call the superclass' setUpClass() method.
        super().setUpClass()

        # Create a client object for the class to make requests.
        cls.client = Client()

    # Test get requests for the home page.
    def test_get(self):
        # Send a get request without a trailing forward slash.
        response = self.client.get('')

        # Ensure that the response has the correct status code and the proper templates were used.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lens/base.html')
        self.assertTemplateUsed(response, 'lens/home.html')

        # Send a get request with a trailing forward slash.
        response = self.client.get('/')

        # Ensure that the response has the correct status code and the proper template was rendered.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lens/base.html')
        self.assertTemplateUsed(response, 'lens/home.html')


# A test case which tests whether emails can successfully be sent with AWS SES.
class SendEmailTestCase(TestCase):
    # Set up the class for testing.
    @classmethod
    def setUpClass(cls):
        # Call the superclass' setUpClass() method.
        super().setUpClass()

        # Add test data to the class.
        cls.email_subject = 'Lens Email Test'
        cls.email_body = 'This is a test email for programmatic email delivery from Lens with AWS SES'
        cls.email_sender = 'Lens Email Test Service <email-test@epm0dev.me>'
        cls.email_recipients = ['epmancin@ncsu.edu']

    # Test whether or not an email can be sent successfully and whether or not it's contents are correct in the outbox.
    def test_send_email(self):
        # Send an email with the class' test data and store the status that is returned.
        status = mail.send_mail(
            self.email_subject,
            self.email_body,
            self.email_sender,
            self.email_recipients,
            fail_silently=False,
        )

        # Ensure that the returned status code is not 0 (i.e. the email was successfully sent).
        self.assertNotEqual(status, 0)

        # Ensure that the length of the mail outbox is correct.
        self.assertEqual(len(mail.outbox), 1)

        # Ensure that the contents of the email are correct.
        self.assertEqual(mail.outbox[0].subject, self.email_subject)
        self.assertEqual(mail.outbox[0].body, self.email_body)
