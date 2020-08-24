from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "brainSkills/layout.html")


def carina(request):
    return HttpResponse("Hello, Carina!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
