from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response

# Create your views here.
class StudentData(APIView):
    def get(self, request, format = None): # this is get method 

        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many = True)

        return Response({
            "status":True,
            "message":"All student data fetched successfully",
            "data":serializer.data
        })
