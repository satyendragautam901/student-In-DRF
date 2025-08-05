from rest_framework import serializers
from api.models import Student

class StudentModelSerializer(serializers.ModelSerializer): # be careful here during importing modelserializer
    class Meta:
        model = Student
        fields = '__all__'