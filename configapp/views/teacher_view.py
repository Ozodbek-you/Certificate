from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from configapp.models import Teacher
from configapp.serializers import *
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings

class TeacherCreateApi(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = UserAndTeacherSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserAndTeacherSerializer
        return TeacherSerializer


    def create(self, request, *args, **kwargs):
        user_data = request.data.get('user', None)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save(is_teacher=True)
        else:
            print("USER ERRORS:", user_serializer.errors)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        teacher = request.data.get('teacher', None)
        teacher_serializer = TeacherSerializer(data=teacher)
        if teacher_serializer.is_valid():
            teacher_serializer.save(user=user)
        else:
            print("TEACHER ERRORS:", teacher_serializer.errors)
            user.delete()
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "user": user_serializer.data,
            "teacher": teacher_serializer.data
        }, status=status.HTTP_201_CREATED)

class DepartmentAPI(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class CourseAPI(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
