from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all-students/', ListStudentMixin.as_view()),
    path('get-student/<int:pk>', RetrieveStudentMixin.as_view()), # get single instance
    path('create-student/', CreateStudentMixin.as_view()), # create record 
    path('update-student/<int:pk>', UpdateStudentMixin.as_view()), # partial update data
    path('full-update-student/<int:pk>', FullUpdateStudent.as_view()), # full update data
    path('delete-student/<int:pk>', DeleteStudentMixin.as_view()), # delete student

    # this url handles all the crud operation in single place
    path('students/', StudentCRUDView.as_view()),          # list & create
    path('students/<int:pk>/', StudentCRUDView.as_view()), # retrieve, update, delete
    

]