from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('all-students/', get_student),
    path('all-students-json/', get_student_json),
    path('create-student/', create_student),
    path('update-student/<int:pk>', update_stu),

]