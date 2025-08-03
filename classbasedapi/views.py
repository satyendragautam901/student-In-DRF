from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentData(APIView):
    def get(self, request, format = None): # this is get method 

        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many = True)

        return Response({
            "status":True,
            "message":"All student data fetched successfully",
            "data":serializer.data
        }, status= status.HTTP_200_OK)
    
    def post(self, request, format = None):

        if(request.method == "POST"):
            serializer = StudentModelSerializer(data = request.data)
            
            if(serializer.is_valid()): # if the data is valid then save

                serializer.save()

                return Response({
                "status":True,
                "message":"student data created successfully",
                "data":serializer.data
                }, status= status.HTTP_201_CREATED)
            
            return Response({ # return if any error happen during validating data
                "status":False,
                "message":"Error while creating data",
                "data":serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
