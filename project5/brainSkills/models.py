import json
from django.forms.models import model_to_dict
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_guest = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    price = models.FloatField()

    def _str_(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="users")
    service = models.ManyToManyField(
        Service, related_name="services")
    level = models.ManyToManyField(
        Level, related_name="levels")

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="message")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.content


class Class(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    day = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        start_time = self.start.strftime("%H:%M")  # '07:00'
        end_time = self.end.strftime("%H:%M")      # '07:50'
        return "{} ({} - {})".format(self.day, start_time, end_time)
        # 'Course 1 (07:00 - 07:50)
