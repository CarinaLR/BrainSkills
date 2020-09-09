from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login", views.login_in, name="login"),
    path("status", views.status, name="status"),
    path("change_status", views.change_status, name="change_status"),
    path("logout", views.logout_out, name="logout"),
    path("<str:name>", views.greet, name="greet")
]
