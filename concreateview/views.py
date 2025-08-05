from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentModelSerializer
from api.models import Student

# Create your views here.
class ListStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

