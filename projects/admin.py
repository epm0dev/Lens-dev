from django.contrib import admin
from .models import Project, GithubContent
from django.utils import timezone


# TODO Documentation
class GithubContentAdmin(admin.StackedInline):
    # TODO Documentation
    model = GithubContent

    # Exclude the id field from being displayed when viewing github content entries.
    exclude = ('id',)

    # TODO Documentation
    extra = 1

    verbose_name = 'Github Content Item'
    verbose_name_plural = 'Github Content Items'


# An admin model which allows superusers to add, view, edit and delete project entries in the database.
@admin.register(Project, site=admin.site)
class ProjectAdmin(admin.ModelAdmin):
    # Set the value to display in the case of an empty field.
    empty_value_display = '-empty-'

    # TODO Documentation
    fields = (
        ('id', 'title', '_status'),
        ('start_date', 'completion_date'),
        'description',
        'details'
    )

    # TODO Documentation
    readonly_fields = ('id',)

    # TODO Documentation
    def mark_in_progress(self, request, queryset):
        queryset.filter(_status=Project.Status.FUTURE).update(start_date=timezone.now())
        queryset.update(_status=Project.Status.IN_PROGRESS)
    mark_in_progress.short_description = 'Mark selected projects as in progress'

    # TODO Documentation
    def mark_paused(self, request, queryset):
        queryset.filter(_status=Project.Status.FUTURE).update(start_date=timezone.now())
        queryset.update(_status=Project.Status.PAUSED)
    mark_paused.short_description = 'Mark selected projects as paused'

    # TODO Documentation
    def mark_completed(self, request, queryset):
        queryset.update(_status=Project.Status.COMPLETED, completion_date=timezone.now())
    mark_completed.short_description = 'Mark selected projects as completed'

    # TODO Documentation
    actions = ['mark_in_progress', 'mark_paused', 'mark_completed']

    # Add the ability to filter projects on the project admin page by status.
    list_filter = ('_status',)

    # TODO Documentation
    inlines = [GithubContentAdmin]
