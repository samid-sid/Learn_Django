from rest_framework import serializers
from .models import Students , Course



class Course_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Student_Serialize(serializers.ModelSerializer):
    course = serializers.StringRelatedField(
        many = True,
        read_only = True,

    )
    class Meta:
        model = Students
        fields = '__all__'
        