from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView,ListCreateAPIView
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

class UpdateStudent(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class DeleteStudent(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class ListandCreateStudent(ListCreateAPIView): # this will handle both list student and create student
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer