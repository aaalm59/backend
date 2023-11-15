from django.contrib import admin

# Register your models here.


# admin.py

from django.contrib import admin
from app.models import Teacher, Student, Course, Class

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'phone_number', 'date_of_birth')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'start_date', 'end_date')
    filter_horizontal = ('teachers', 'students')
