from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from .serializers import StudentModelSerializer
from api.models import Student

# Create your views here.
class ListStudent(ListAPIView): # no need to write def get.list . It already inbuilt in this
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class GetStudent(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class CreateStudent(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer