from dotenv import load_dotenv

from django.http import HttpResponse
from django.shortcuts import render

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

# block to render contact page


def register(request):
    return render(request, "brainSkills/register.html")

# Block to render greet


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
