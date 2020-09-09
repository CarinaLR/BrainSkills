import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse
from dotenv import load_dotenv

from .models import User, Service, Level, Student, Teacher, Message


# Create your views here.

load_dotenv()

# Block to render index page


def index(request):

    return render(request, "brainSkills/index.html")

# Block to render about our company


def about(request):
    return render(request, "brainSkills/about.html")

# block to render services


def services(request):
    return render(request, "brainSkills/services.html")

# block to render contact page


def contact(request):
    return render(request, "brainSkills/contact.html")

# block to render register page


def register(request):
    if request.method == "POST":
        username = request.POST["full_name"]
        email = request.POST["email"]

        # Confirmation password
        password = request.POST["password"]
        confirmation = request.POST["con_pass"]
        if password != confirmation:
            return render(request, "brainSkills/register.html", {
                "message": "Password must match."
            })

        # Create User
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "brainSkills/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "brainSkills/register.html")

# block to login contact page


def login_in(request):
    if request.method == "POST":
        # Sign user in
        username = request.POST["full_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
                            emai=email, password=password)

        # Authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "brainSkills/login.html", {
                "message": "Invalid Full Name, Email or Password."
            })
    else:
        return render(request, "brainSkills/login.html")


# Block to log the user out


def logout_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Block to render greet


def profile(request, name):
    # user = request.user

    # if user == name:

    #     if user.is_student == False and user.is_teacher == False and user.is_guest == False:
    #         login(request, user)

    #         return HttpResponseRedirect(reverse("status"))
    return render(request, "brainSkills/user_type.html", {
        "username": name.capitalize()
    })


def student_login(request):
    return render(request, "brainSkills/user_type.html")


def teacher_login(request):
    return render(request, "brainSkills/user_type.html")
