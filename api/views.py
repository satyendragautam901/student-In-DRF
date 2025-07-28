from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.

# show all student data
@api_view(['get'])
def get_student(request):
    student = Student.objects.all()

    serializer = StudentSerializer(student, many = True)

    return Response(serializer.data)

def get_student_json(request):
    student = Student.objects.all()

    serializer = StudentSerializer(student, many = True)

    return JsonResponse(serializer.data,safe= False)
        
# create a student

@api_view(['post'])
def create_student(request):
    data = request.data
    print("requested data ", data)
    serializer = StudentSerializer(data = data) # here be carefull

    if(serializer.is_valid()):
        try:
            serializer.save()
            return JsonResponse({
                "status":True,
                "data":serializer.data,
                "message":"student created successfully"
            })

        except Exception as e:
            return JsonResponse({
                "status": False,
                "data": serializer.errors,
                "message": f"Error during creating student: {str(e)}"
            })
        
    return JsonResponse({
                "status":False,
                "data":serializer.errors,
                "message":"Error please try again after some time"
            })

    