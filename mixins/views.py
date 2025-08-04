from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from api.models import Student
from .serializers import StudentModelSerializer

# Create your views here.
class ListStudentMixin(ListModelMixin,GenericAPIView): # list all the record from db
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class CreateStudentMixin(CreateModelMixin, GenericAPIView): # create an instance in db
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RetrieveStudentMixin(RetrieveModelMixin, GenericAPIView): # get single instance from db
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs): # no need to pass pk here, drf will automatically do this and pass to **kwargs
        return self.retrieve(request,*args, **kwargs)
    
class UpdateStudentMixin(UpdateModelMixin, GenericAPIView): # update instance only few part(partial update)
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args,**kwargs) # here make sure to call partial_update
    
class FullUpdateStudent(UpdateModelMixin, GenericAPIView):  # full update
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) # here pass self.put for full update
    
class DeleteStudentMixin(DestroyModelMixin, GenericAPIView): # delete record
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) # here pass self.delete for delete
    
class StudentCRUDView(ListModelMixin, 
                      CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin,
                      GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
