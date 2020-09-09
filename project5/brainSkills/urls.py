from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login", views.login_in, name="login"),
    path('login/student/', views.student_login, name='student_login'),
    path('login/teacher/', views.teacher_login, name='teacher_login'),
    path("logout", views.logout_out, name="logout"),
    path("<str:name>", views.profile, name="profile"),
    path("status/<str:status>", views.status, name="status")
]
