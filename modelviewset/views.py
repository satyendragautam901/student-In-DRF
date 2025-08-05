from django.shortcuts import render
from .serializers import StudentModelSerializer
from api.models import Student
from rest_framework import viewsets

# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet): # all the CRUD operation in only three lines of code
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet): # only read optionis allowed
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer