from django.shortcuts import render
from rest_framework import viewsets
from api.models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self,request): # list all the record 
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many = True)
        return Response({
            "status":True,
            "message":"student data",
            "data":serializer.data
        },status= status.HTTP_200_OK)
    
    def retrieve(self, request, pk): # get single instance from db
        try:
            stu = Student.objects.get(id = pk)

        except Student.DoesNotExist:
            return Response({
                "status":False,
                "message":f"Student record is no found with this id {pk}"
                
            }, status=status.HTTP_200_OK)
        serializer = StudentModelSerializer(stu)

        return Response({
            "status":True,
            "message":"student record is found",
            "data":serializer.data
        })

    
    def create(self, request): # create record in db
        serializer = StudentModelSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "status":True,
                "message":"student created successfully",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
                "status":False,
                "message":"error during creating student",
                "data":serializer.errors
            })
    
    def update(self, request, pk=None):
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({
                "status": False,
                "message": f"Student record not found with id {pk}"
            }, status=404)

        serializer = StudentModelSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Student record updated successfully",
                "data": serializer.data
            })
        
        return Response({
            "status": False,
            "message": "Error during updating student",
            "data": serializer.errors
        })


    def partial_update(self, request, pk=None):
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({
                "status": False,
                "message": f"Student record not found with id {pk}"
            }, status=404)

        serializer = StudentModelSerializer(stu, data=request.data, partial=True)  # ✅ add partial=True
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Student record partially updated",
                "data": serializer.data
            })
        
        return Response({
            "status": False,
            "message": "Error during partial update",
            "data": serializer.errors
        })


    def destroy(self, request, pk=None):
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({
                "status": False,
                "message": f"Student record not found with id {pk}"
            }, status=404)

        serialized_data = StudentModelSerializer(stu).data  # ✅ serialize before delete
        stu.delete()
        return Response({
            "status": True,
            "message": "Student record deleted successfully",
            "data": serialized_data
        })

            
        
        
