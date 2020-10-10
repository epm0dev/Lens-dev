from django.test import SimpleTestCase, Client
import requests
from .views import ResumeView


# A test case for the resume page.
class ResumePageTestCase(SimpleTestCase):
    # Set up the class for testing.
    @classmethod
    def setUpClass(cls):
        # Call the superclass' setUpClass() method.
        super().setUpClass()

        # Create a client object for the class to make requests.
        cls.client = Client()

    # Test get requests for the resume page.
    def test_get(self):
        # Send a get request without a trailing forward slash.
        response = self.client.get('/resume')

        # Ensure that the response has the correct status code and the proper templates were used.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lens/base.html')
        self.assertTemplateUsed(response, 'resume/resume.html')

        # Send a get request with a trailing forward slash.
        response = self.client.get('/resume/')

        # Ensure that the response has the correct status code and the proper template was rendered.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lens/base.html')
        self.assertTemplateUsed(response, 'resume/resume.html')

    # Test that the resume can be successfully downloaded from the download path.
    def test_download(self):
        # Ensure that a get request to the download path of the resume returns a response with status code 200.
        self.assertEqual(requests.get(ResumeView.download_path).status_code, 200)
