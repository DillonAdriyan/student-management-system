from rest_framework import serializers
from .models import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        

class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Gunakan CourseSerializer untuk menampilkan data course

    class Meta:
        model = Student
        fields = '__all__'


