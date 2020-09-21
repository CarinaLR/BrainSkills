from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("accounts", views.accounts, name="accounts"),
    path("register_guest", views.register, name="register"),
    path("login", views.login_in, name="login"),
    path('login/student/', views.student_login, name='student_login'),
    path('login/teacher/', views.teacher_login, name='teacher_login'),
    path("logout", views.logout_out, name="logout"),
    path("user_info/<int:user_id>", views.user_info, name="user_info"),
    path("<str:name>", views.profile, name="profile"),
    path("new_message", views.new_message, name="new_message"),
    path("status/<str:status>", views.status, name="status"),
]
