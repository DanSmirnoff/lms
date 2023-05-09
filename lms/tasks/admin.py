from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Task, Teacher, Student, StudentGroup, Mark, StudentGroupStudent


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)
    empty_value_display = '-null-'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'view_groups_link')
    search_fields = ('user', )

    def view_groups_link(self, obj):
        count = obj.group.count()
        url = (
            reverse("admin:tasks_studentgroup_changelist")
            + "?"
            + urlencode({"students__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {} Groups</a>', url, count)

    view_groups_link.short_description = 'Groups'
    empty_value_display = '-null-'


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'task', 'value')
    search_fields = ('student', 'task', 'value')
    empty_value_display = '-null-'


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_students_link')

    def view_students_link(self, obj):
        count = obj.students.count()
        url = (
            reverse("admin:tasks_student_changelist")
            + "?"
            + urlencode({"group__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {} Students</a>', url, count)

    view_students_link.short_description = 'Students'
    empty_value_display = '-null-'


@admin.register(StudentGroupStudent)
class StudentGroupStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'student_group')
    empty_value_display = '-null-'


admin.site.register(Teacher)
