from django.contrib import admin
from django.urls import path,include
from users import views
urlpatterns = [
    path('login/',views.loginView,name="login"),
    path('register/',views.signupView,name="register"),
    path('profile/',views.profileView,name="profile"),
    ]