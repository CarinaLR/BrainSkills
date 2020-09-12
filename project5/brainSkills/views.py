import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
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


def accounts(request):
    return render(request, "brainSkills/user_type.html")


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
    username = request.user

    # Base in user_type get user information to display on profile page
    if username.is_student == False and username.is_teacher == False and username.is_guest == False:
        return render(request, "brainSkills/user_type.html")

    if username.is_student == True and username.is_teacher == False and username.is_guest == False:

        student = Student.objects.get(user=username)
        print("STUDENT ", student)
        service = student.service.all()
        print("SERVICE ", service)
        level = student.level.all()
        print("LEVEL ", level)
        return render(request, "brainSkills/profile_student.html")

    if username.is_student == False and username.is_teacher == True and username.is_guest == False:
        return render(request, "brainSkills/profile_teacher.html")

    if username.is_student == False and username.is_teacher == False and username.is_guest == True:
        return render(request, "brainSkills/services.html")

    return render(request, "brainSkills/student_login.html", {
        "username": name.capitalize()
    })


@login_required
def status(request, status):
    print("reach Status view")
    queryset = User.objects.all()
    username = request.user

    if request.method == "GET":
        user_id = username.id
        user_is_student = username.is_student
        user_is_teacher = username.is_teacher
        user_is_guest = username.is_guest
        response = {"username": username, "user_id": user_id, "user_is_student": user_is_student,
                    "user_is_teacher": user_is_teacher, "user_is_guest": user_is_guest}

    return JsonResponse(response, safe=False)


def student_login(request):
    if request.method == "POST":
        # Get all information from user_type student
        username = request.POST["full_name"]
        email = request.POST["email"]
        service = request.POST["services"]
        print("service -", service)
        # Convert string from input into integer to pass as id filed for service
        service_id = print(int(service))
        # Convert string from input into integer to pass as id filed for level
        level = request.POST["levels"]
        print("level -", level)
        level_id = print(int(level))

        # Retrieve information from Service table and Level table
        query_set_services = Service.objects.all()
        print("query_service -", query_set_services)
        query_set_levels = Service.objects.all()
        print("query_level -", query_set_levels)

        # Confirmation password
        password = request.POST["password"]
        confirmation = request.POST["con_pass"]
        if password != confirmation:
            return render(request, "brainSkills/register.html", {
                "message": "Password must match."
            })

        # Create User update is_student to True
        try:
            user = User.objects.create_user(username, email, password)
            user.is_student = True
            user.save()
        # Create Student adding extra information
            student = Student.objects.create(user=user)
            print("STUDENT - ", student)
            student.service.add(service_id)
            student.level.add(level_id)
        except IntegrityError:
            return render(request, "brainSkills/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "brainSkills/student_login.html")


def teacher_login(request):
    if request.method == "POST":
        # Get all information from user_type student
        username = request.POST["full_name"]
        email = request.POST["email"]

        # Confirmation password
        password = request.POST["password"]
        confirmation = request.POST["con_pass"]
        if password != confirmation:
            return render(request, "brainSkills/register.html", {
                "message": "Password must match."
            })

        # Create User update is_teacher to True
        try:
            user = User.objects.create_user(username, email, password)
            user.is_teacher = True
            user.save()
        # Create Teacher with user information
            teacher = Teacher.objects.create(user=user)
            print("TEACHER - ", teacher)

        except IntegrityError:
            return render(request, "brainSkills/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "brainSkills/teacher_login.html")
