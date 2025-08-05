from django.shortcuts import render
from rest_framework import viewsets
from api.models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response


# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        try:
            stu = Student.objects.get(id = pk)

        except Student.DoesNotExist:
            return Response({
                "status":False,
                "message":f"Student record is no found with this id {pk}"
                
            })
        serializer = StudentModelSerializer(stu)

        return Response({
            "status":True,
            "message":"student record is found",
            "data":serializer.data
        })

    
    def create(self, request):
        serializer = StudentModelSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)