from django.contrib import admin

from .models import Task, Teacher, Student, StudentGroup, Mark


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)
    empty_value_display = '-null-'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    search_fields = ('user', 'group')
    empty_value_display = '-null-'


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'task', 'value')
    search_fields = ('student', 'task', 'value')
    empty_value_display = '-null-'


admin.site.register(Teacher)
admin.site.register(StudentGroup)
