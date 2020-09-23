from django.core import mail
from django.test import TestCase


# TODO Documentaion
class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail(
            'That’s your subject', 'That’s your message body',
            'from@yourdjangoapp.com', ['to@yourbestuser.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'That’s your subject')
        self.assertEqual(mail.outbox[0].body, 'That’s your message body')