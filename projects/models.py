from django.db import models
from django.utils.translation import gettext_lazy as _
from itertools import chain
from operator import attrgetter


# A model which represents a projects to be displayed on the projects page of the website.
class Project(models.Model):
    # Define the possible statuses of a project, each with a function to get their full text.
    class Status(models.TextChoices):
        FUTURE = 'F', _('Future')  # The project has not been started yet, but is planned to be completed.
        IN_PROGRESS = 'I', _('In Progress')  # The project has been started and is actively being worked on.
        PAUSED = 'P', _('Paused')  # The project has been started, but it is not actively being worked on.
        COMPLETED = 'C', _('Completed')  # The project has been completed.

    # Explicitly define an integer primary key for a project entry.
    id = models.IntegerField(primary_key=True, auto_created=True)

    # Fields which contain a project's title, status, description, and extended details.
    title = models.CharField(max_length=200, null=False, unique=True)
    _status = models.CharField(max_length=1, choices=Status.choices, default=Status.FUTURE)
    description = models.TextField(max_length=3000, default='')
    details = models.TextField(default='')

    # Fields which contain the start and end dates of a project.
    start_date = models.DateField(null=True)
    completion_date = models.DateField(null=True)

    # A property which acts as shortcut for accessing the full display string of a project's status.
    @property
    def status(self):
        return self.get__status_display()

    # A property which returns a string containing a small message describing the project's status.
    @property
    def status_tooltip(self):
        # Return the appropriate string based on the project's status.
        if self._status == self.Status.FUTURE:
            return 'This project has not yet been started.'
        elif self._status in [self.Status.IN_PROGRESS, self.Status.PAUSED]:
            return f'This project was started on {self.start_date.strftime("%B %d, %Y")}.'
        elif self._status == self.Status.COMPLETED:
            return f'This project was completed on {self.completion_date.strftime("%B %d, %Y")}.'

    # A property which returns a list containing each paragraph in a project's details field.
    @property
    def details_as_list(self):
        # Define an empty list to store each paragraph and an empty string to store the current paragraph.
        details_list = []
        par = ''

        # Iterate through all of the characters in the project's details field.
        for c in self.details:
            # If a newline character is encountered, add the current paragraph string to the list, empty the current
            # paragraph string and continue to the next loop iteration.
            if c == '\n':
                details_list.append(par)
                par = ''
                continue

            # Otherwise, simply append the current character to the current paragraph string.
            par += c

        # Add the last paragraph to the the list of paragraphs.
        details_list.append(par)

        # Return the list of paragraphs in the project's details field.
        return details_list

    # Define a property which returns a list of all of the project's related content items, sorted by their display
    # priority.
    @property
    def content(self):
        return sorted(
            chain(
                self.projects_githubcontent_related.all(),
            ),
            key=attrgetter('display_priority'),
            reverse=True
        )

    # Define the string representation of a project object.
    def __str__(self):
        return f'{self.title}'


# Define the different types of content models.
class ContentTypes(models.TextChoices):
    GITHUB = 'github', _('Github Repository Preview')


# Define the possible display priorities for the content.
class DisplayPriority(models.IntegerChoices):
    LOW = -1, _('Low')  # The content should be displayed near the bottom of the project card.
    MEDIUM = 0, _('Medium')  # The content should be displayed somewhere in the middle of the project card.
    HIGH = 1, _('High')  # The content should be displayed near the top of the project card.


# The base model for content to be displayed in blocks within a project card.
class AbstractContent(models.Model):
    # Explicitly define an integer primary key for a project entry.
    id = models.IntegerField(primary_key=True, auto_created=True)

    # A field which contains a content item's content type. The available content types are specified by the
    # ContentTypes class.
    content_type = models.CharField(max_length=20, choices=ContentTypes.choices)

    # A field which indicates whether a content entry should be displayed at the start, in the middle (default), or at
    # the end of a project card.
    display_priority = models.IntegerField(choices=DisplayPriority.choices, default=0)

    # A field which represents a Many-To-One relationship from content entries to a single project entry.
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        # Set the field name from which a QueryList of a project's related content entries can be accessed.
        related_name='%(app_label)s_%(class)s_related',
    )

    # Specify that this model class is abstract.
    class Meta:
        abstract = True
        ordering = ['-display_priority']


# A model, which inherits from the AbstractContent model, that represents a block representing a project's github
# repository.
class GithubContent(AbstractContent):
    # Set the content's content type.
    content_type = ContentTypes.GITHUB

    # A field which contains the URL of the github repository of the project.
    repository_url = models.CharField(max_length=200, null=False)

    # A property which returns the path of the template to render the content with.
    @property
    def template(self):
        return 'projects/content/github.html'

    # Define the string representation of a github content object.
    def __str__(self):
        return f'GitHub content for project: "{self.project.title}"'
