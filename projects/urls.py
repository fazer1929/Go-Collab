from django.contrib import admin
from django.urls import path,include
from projects import views
urlpatterns = [
    path('',views.projectView),
    path('addaprove/',views.addUserAproval),
    path('addmembers/',views.addUserAproval),
    path('addcomment/',views.addComments),
]