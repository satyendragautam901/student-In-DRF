from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all-students/', ListStudent.as_view()),
    path('get-student/<int:pk>', GetStudent.as_view()), # get single instance
    path('create-student/', CreateStudent.as_view()), # create record 
    path('update-student/<int:pk>', UpdateStudent.as_view()), # This will work for partial and full update
    
    path('delete-student/<int:pk>', DeleteStudent.as_view()), # delete student

    # # this url handles all the crud operation in single place
    # path('students/', StudentCRUDView.as_view()),          # list & create
    # path('students/<int:pk>/', StudentCRUDView.as_view()), # retrieve, update, delete
    

]