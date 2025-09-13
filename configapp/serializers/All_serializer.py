from rest_framework import serializers
from configapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number','password', 'email', 'is_admin', 'is_active', 'is_student', 'is_teacher']
        read_only_fields = ['sms_kod']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'