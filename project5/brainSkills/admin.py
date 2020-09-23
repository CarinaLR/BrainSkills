from django.contrib import admin

from .models import User, Service, Level, Student, Teacher, Message, Course
# Register your models here.

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Level)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Message)
admin.site.register(Course)
