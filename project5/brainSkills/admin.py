from django.contrib import admin

from .models import User, Service, Level, Student, Teacher, Message, Course, Assign, Schedule
# Register your models here.

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Level)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Message)
admin.site.register(Course)
admin.site.register(Assign)
admin.site.register(Schedule)
