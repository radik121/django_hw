from django.contrib import admin

from .models import Student, Teacher, StudentsTeacher


class STInline(admin.TabularInline):
    model = StudentsTeacher
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['name']
    list_display_links = ['id', 'name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [STInline]
