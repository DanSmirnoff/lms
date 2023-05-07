from django.contrib import admin

from .models import Task


@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)
    empty_value_display = '-null-'
