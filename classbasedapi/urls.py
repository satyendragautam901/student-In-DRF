from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all-students/', StudentData.as_view()),
    

]