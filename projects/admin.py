from django.contrib import admin
from .models import Project, AbstractContent, GithubContent
from django.utils import timezone


# class ContentInline(admin.TabularInline):
#     model = AbstractContent
#     extra = 1


# An admin model which allows superusers to add, view, edit and delete project entries in the database.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Set the value to display in the case of an empty field.
    empty_value_display = '-empty-'

    # TODO Description
    fields = (
        ('id', 'title', '_status'),
        ('start_date', 'completion_date'),
        'description',
    )

    # TODO Description
    readonly_fields = ('id',)

    # TODO Description
    def mark_in_progress(self, request, queryset):
        queryset.filter(_status=Project.Status.FUTURE).update(start_date=timezone.now())
        queryset.update(_status=Project.Status.IN_PROGRESS)
    mark_in_progress.short_description = 'Mark selected projects as in progress'

    # TODO Description
    def mark_paused(self, request, queryset):
        queryset.filter(_status=Project.Status.FUTURE).update(start_date=timezone.now())
        queryset.update(_status=Project.Status.PAUSED)
    mark_paused.short_description = 'Mark selected projects as paused'

    # TODO Description
    def mark_completed(self, request, queryset):
        queryset.update(_status=Project.Status.COMPLETED, completion_date=timezone.now())
    mark_completed.short_description = 'Mark selected projects as completed'

    # TODO Description
    actions = ['mark_in_progress', 'mark_paused', 'mark_completed']

    # Add the ability to filter projects on the project admin page by status.
    list_filter = ('_status',)

    # TODO Description
    # inlines = [
    #     ContentInline,
    # ]


# An admin model which allows superusers to add, view, edit and delete github content entries in the database.
@admin.register(GithubContent)
class GithubContentAdmin(admin.ModelAdmin):
    # Set the value to display in the case of an empty field.
    empty_value_display = '-empty-'

    # Exclude the id field from being displayed when viewing github content entries.
    exclude = ('id',)

    # Add the title of a github content entry's project foreign key to be searched on the github content admin page.
    search_fields = ['project__title']
