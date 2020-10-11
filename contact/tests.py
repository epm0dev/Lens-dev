from django.test import TestCase, Client


# A test case for the contact page's GET and POST requests.
class ContactPageTestCase(TestCase):
    # Set up the class for testing.
    @classmethod
    def setUpClass(cls):
        # Call the superclass' setUpClass() method.
        super().setUpClass()

        # Create a client object for the class to make requests.
        cls.client = Client()

        # Define valid post data for the contact form.
        cls.valid_data = {
            'first-name': 'Ethan',
            'last-name': 'Mancini',
            'middle-initial': 'P',
            'email-address': 'epmancin@ncsu.edu',
            'phone-number': '330-322-6010',
            'message': 'Message'
        }

        # Define invalid post data for the contact form.
        cls.invalid_data = {
            'first-name': '',
            'last-name': '',
            'middle-initial': None,
            'email-address': 'invalid.edu',
            'phone-number': '111-2222-33A',
            'message': ''
        }

    # Test get requests for the contact page.
    def test_get(self):
        # Send a get request without a trailing forward slash.
        response = self.client.get('/contact')

        # Ensure that the response has the correct status code and the proper template was rendered.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lens/base.html')
        self.assertTemplateUsed(response, 'contact/contact.html')

        # Send a get request with a trailing forward slash.
        response = self.client.get('/contact/')

        # Ensure that the response has the correct status code and the proper template was rendered.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lens/base.html')
        self.assertTemplateUsed(response, 'contact/contact.html')

    # Test post requests for the contact page.
    def test_post(self):
        # Attempt to make a post request with each combination of mostly valid data with one invalid field.
        for key in self.invalid_data:
            # If the value in invalid_data associated with the current key is None, the field cannot be invalid, so
            # continue to the next iteration of the loop.
            if self.invalid_data[key] is None:
                continue

            # Copy the valid data to a new dictionary.
            post_data = self.valid_data.copy()

            # Replace the valid value at the current key with an invalid one.
            post_data[key] = self.invalid_data[key]

            # Send a post request containing the data and ensure that the response has a status code of 400.
            response = self.client.post('/contact', data=post_data)
            self.assertEqual(response.status_code, 400)

        # Send a post request containing the valid data and ensure that the response has an error code less than 400.
        response = self.client.post('/contact', data=self.valid_data)
        self.assertLess(response.status_code, 400)
