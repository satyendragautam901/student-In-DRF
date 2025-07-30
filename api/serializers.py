from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance is old data, while validate_data is new data.

        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)

        instance.save()

        return instance
    
    def validate_city(self, value): # field level validation
        if value == "UAE":
            raise serializers.ValidationError("Foreign student is not accepted right now ")

        return value
    
    def validate(self, data):
        roll = data.get('roll')
        name = data.get('name')

        if name == "adi" and roll == 3:
            raise serializers.ValidationError("This is defaulter student")
        return data
     
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__' # this will include all the fields of model eg: name, city, roll
        # same as fields = ['name', 'city', 'roll']
        # some property read_only, exclude etc.