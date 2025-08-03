from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all-students/', StudentData.as_view()),
    path('create-student/', StudentData.as_view()),
    path('update-student/<int:pk>', StudentData.as_view()),
    path('delete-student/<int:pk>', StudentData.as_view()),
    

]