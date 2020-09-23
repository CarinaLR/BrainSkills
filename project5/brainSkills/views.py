import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt

from .models import User, Service, Level, Student, Teacher, Message, Course, Assign, Schedule


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

        # Gert student by username
        student = Student.objects.get(user=username)
        print("STUDENT ", student)

        # Access to service query_set and get service name
        service = student.service.all()
        service_name = service[0].name
        print("service_name ", service_name)

        # Access to level query_set and get level name
        level = student.level.all()
        level_name = level[0].name
        print("level_name ", level_name)
        return render(request, "brainSkills/profile_student.html", {
            "student": student,
            "service": service_name,
            "level": level_name
        })

    if username.is_student == False and username.is_teacher == True and username.is_guest == False:

        teacher = Teacher.objects.get(user=username)
        students = Student.objects.all()
        print("Student_list", students)
        for student in students:
            print("Student_name", student.user.username)

        return render(request, "brainSkills/profile_teacher.html", {
            "teacher": teacher,
            "students": students
        })

    if username.is_student == False and username.is_teacher == False and username.is_guest == True:
        return render(request, "brainSkills/services.html")

    return render(request, "brainSkills/student_login.html", {
        "username": name.capitalize()
    })


@login_required
def status(request, status):
    print("reach Status view")
    queryset = User.objects.all()
    print("allUsers - ", queryset)
    username = request.user
    print("username - ", username)

    if request.method == "GET":
        # Query for requested user
        user = User.objects.get(username=request.user, pk=request.user.id)
        print("user -", user)

        user_id = user.id
        email = user.email
        password = user.password
        user_is_student = user.is_student
        user_is_teacher = user.is_teacher
        user_is_guest = user.is_guest

        # Serialize response
        response = {
            "username": user.username,
            "user_id": user_id,
            "user_email": email,
            "user_is_student": user.is_student,
            "user_is_teacher": user.is_teacher,
            "user_is_guest": user.is_guest
        }
        print("response -", response)
        data = json.dumps(response)

    return JsonResponse(data, safe=False)


def user_info(request, user_id):
    print("reach user_info", user_id)
    current_user = User.objects.get(pk=user_id)
    username = request.user

    # Return user info
    if request.method == "GET":
        # Query for requested user
        user = User.objects.get(username=request.user, pk=request.user.id)

        user_id = user.id
        email = user.email
        password = user.password
        user_is_student = user.is_student
        user_is_teacher = user.is_teacher
        user_is_guest = user.is_guest

        # Serialize response
        response = {
            "username": user.username,
            "user_id": user_id,
            "user_email": email,
        }
        data = json.dumps(response)
        print("DATA - ", data)
        return JsonResponse(data, safe=False)

    print("reach route new_message")

    message = request.POST.get("w_message")
    # Get POST request to create message
    if request.method == "POST":
        # Get user instance
        user = User.objects.get(username=request.user, pk=request.user.id)
        # Get contents of email
        back_data = json.loads(request.body)
        content = back_data
        print("message -", content)

        # Get variables
        owner = user
        new_content = content
        print("OWNER ", owner)
        print("MESSAGE ", new_content)
        # Save message getting information from api post request.
        message = Message.objects.create(
            owner=owner, content=new_content)
        message.save()
        return JsonResponse({"message": "Message sent successfully."}, status=201)
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

    return HttpResponse(status=204)


def student_login(request):
    if request.method == "POST":
        # Get all information from user_type student
        username = request.POST["full_name"]
        email = request.POST["email"]
        service = request.POST["services"]
        # Convert string from input into integer to pass as id filed for service
        service_id = int(service)
        # Convert string from input into integer to pass as id filed for level
        level = request.POST["levels"]
        level_id = int(level)

        # Retrieve information from Service table and Level table
        query_set_services = Service.objects.all()
        user_service = Service.objects.get(pk=service_id)

        query_set_levels = Service.objects.all()
        user_level = Service.objects.get(pk=level_id)

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
            # Add student to the service query set
            student.service.add(service_id)

            # Add student to the level query set
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
