from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("carina", views.carina, name="carina"),
    path("<str:name>", views.greet, name="greet")
]
