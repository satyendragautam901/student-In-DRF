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
                }, status=status.HTTP_400_BAD_REQUEST) # status code is helpful to understand exact issue
    
    # partial update record
        
    def patch(self, request, pk, format=None):
        # 1. Try to find the student by ID
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({
                "status": False,
                "message": f"Student with ID {pk} not found."
            }, status=status.HTTP_404_NOT_FOUND)
        
        # 2. Pass existing object + request data to serializer
        serializer = StudentModelSerializer(stu, data=request.data, partial=True) # if i remove partial = true from here it works well for update all fields

        # 3. Validate and save if valid
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Student record updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        # 4. If not valid, return validation error
        return Response({
            "status": False,
            "message": "Error during updating student record",
            "errors": serializer.errors  # changed key from `error` → `errors`
        }, status=status.HTTP_400_BAD_REQUEST)
        

