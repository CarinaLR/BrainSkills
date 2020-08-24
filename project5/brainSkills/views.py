from dotenv import load_dotenv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

load_dotenv()


def index(request):
    return render(request, "brainSkills/index.html")


def carina(request):
    return HttpResponse("Hello, Carina!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
