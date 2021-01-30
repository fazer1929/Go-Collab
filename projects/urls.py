from django.contrib import admin
from django.urls import path,include
from projects import views
urlpatterns = [
    path('',views.projectView,name="index"),
    path('addaprove/',views.addUserAproval,name="add_aprove"),
    path('addmembers/',views.addUserAproval,name="add_members"),
    path('addcomment/',views.addComments,name="add_comments"),
    path('projects/',views.projects,name="projects"),
    path('contact/',views.contact,name="contact"),
    path('create/',views.projectView,name="create-project"),
]