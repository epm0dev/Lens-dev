from django.core import mail
from django.test import TestCase


class HomePageTestCase(TestCase):
    def setUp(self):
        pass


class RepoCacheTestCase(TestCase):
    def setUp(self):
        pass


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
