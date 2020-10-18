from django.test import TestCase


# A test case for the project page's GET requests.
class ProjectPageTestCase(TestCase):
    # Specify the fixture to load for testing the project model.
    fixtures = ['project_fixture.json']

    # Set up the class for testing.
    @classmethod
    def setUpClass(cls):
        # Call the superclass' setUpClass() method.
        super().setUpClass()

        # Define a list containing the templates used to render the projects home page.
        cls.templates = [
            'lens/base.html',
            'projects/home.html',
            'projects/project/card.html',
            'projects/project/detail.html',
            'projects/content/base.html',
            'projects/content/description.html',
            'projects/content/github.html',
        ]

    # Test get requests for the projects page.
    def test_get(self):
        # Send a get request without a trailing forward slash.
        response = self.client.get('/projects')

        # Ensure that the response has the correct status code and the proper templates were rendered.
        self.assertEqual(response.status_code, 200)
        for t in self.templates:
            self.assertTemplateUsed(response, t)

        # Send a get request with a trailing forward slash.
        response = self.client.get('/projects/')

        # Ensure that the response has the correct status code and the proper templates were rendered.
        self.assertEqual(response.status_code, 200)
        for t in self.templates:
            self.assertTemplateUsed(response, t)
