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

    
@api_view(['PATCH'])  # PATCH = partial update
def update_stu(request, pk):
    try:
        record = Student.objects.get(id=pk)

    except Student.DoesNotExist: # doesn't exist work without model
        return JsonResponse({
            "status": False,
            "message": f"Student with id {pk} not found."
        }, status=404)
    
    serializer = StudentSerializer(record, data=request.data, partial=True) # partial = true must hai

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({
            "status": True,
            "data": serializer.data,
            "message": "Student record updated successfully"
        })
    
    return JsonResponse({
        "status": False,
        "data": serializer.errors,
        "message": "Error during updating student record"
    }, status=400)


@api_view(['DELETE'])
def delete_stu(request, pk):
    try:
        student = Student.objects.get(id=pk)

        # Serialize the student *before* deleting
        serializer = StudentSerializer(student)
        student.delete()

        return JsonResponse({
            "status": True,
            "message": f"Student with ID {pk} deleted successfully",
            "deleted_data": serializer.data
        })

    except Student.DoesNotExist:
        return JsonResponse({
            "status": False,
            "message": f"Student with ID {pk} not found"
        }, status=404)

