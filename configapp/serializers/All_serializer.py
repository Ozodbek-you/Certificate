from rest_framework import serializers
from configapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['password', 'email', 'is_admin', 'is_active', 'is_student', 'is_teacher']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'user']
        read_only_fields = ['user']

class UserAndTeacherSerializer(serializers.Serializer):
    user = UserSerializer()
    teacher = TeacherSerializer()


class SendEmail(serializers.Serializer):
    text = serializers.CharField()
    email = serializers.EmailField()

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    verify_kod =serializers.CharField()