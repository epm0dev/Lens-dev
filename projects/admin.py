from django.contrib import admin
from .models import Project, GithubContent
from django.utils import timezone


# A stacked inline admin model which allows github content items to be created via a project admin page and, therefore,
# directly associated with a project rather than having to specify the relationship manually.
class GithubContentAdmin(admin.StackedInline):
    # Define the model that the class is associated with.
    model = GithubContent

    # Exclude the id field from being displayed when viewing github content entries.
    exclude = ('id',)

    # Specify how many additional new github content fields to display after the project's current one(s), if any.
    extra = 1

    # Specify the verbose name and verbose plural name of the class.
    verbose_name = 'Github Content Item'
    verbose_name_plural = 'Github Content Items'


# An admin model which allows superusers to add, view, edit and delete project entries in the database.
# noinspection PyUnusedLocal
@admin.register(Project, site=admin.site)
class ProjectAdmin(admin.ModelAdmin):
    # Set the value to display in the case of an empty field.
    empty_value_display = '-empty-'

    # Specify what project model fields to display and in what orientation.
    fields = (
        ('id', 'title', '_status'),
        ('start_date', 'completion_date'),
        'description',
        'details'
    )

    # Specify the fields which should not be editable.
    readonly_fields = ('id',)

    # Define a custom admin action to mark the selected projects as being in progress.
    def mark_in_progress(self, request, queryset):
        # Update the start date of any projects in the query set with a status of 'future'.
        queryset.filter(_status=Project.Status.FUTURE).update(start_date=timezone.now())

        # Update the projects in the queryset as being in progress.
        queryset.update(_status=Project.Status.IN_PROGRESS)

    # Specify a short description for the custom admin action.
    mark_in_progress.short_description = 'Mark selected projects as in progress'

    # Define a custom admin action to mark the selected projects as being paused.
    def mark_paused(self, request, queryset):
        # Update the start date of any projects in the query set with a status of 'future'.
        queryset.filter(_status=Project.Status.FUTURE).update(start_date=timezone.now())

        # Update the projects in the queryset as being paused.
        queryset.update(_status=Project.Status.PAUSED)

    # Specify a short description for the custom admin action.
    mark_paused.short_description = 'Mark selected projects as paused'

    # Define a custom admin action to mark the selected projects as completed.
    def mark_completed(self, request, queryset):
        # Update the status of the projects in the query set and set their completion date to the current date.
        queryset.update(_status=Project.Status.COMPLETED, completion_date=timezone.now())

    # Specify a short description for the custom admin action.
    mark_completed.short_description = 'Mark selected projects as completed'

    # Specify that the custom admin actions defined above should be displayed.
    actions = ['mark_in_progress', 'mark_paused', 'mark_completed']

    # Add the ability to filter projects on the project admin page by status.
    list_filter = ('_status',)

    # Add the github content stacked inline admin model to the project admin page.
    inlines = [GithubContentAdmin]
