from django.urls import path,include
from rest_framework.routers import DefaultRouter

from configapp.views.student_view import StudentDetailApi, StudentListApi
from configapp.views.teacher_view import TeacherListApi, TeacherDetailApi
from configapp.views.user_view import UserApi

router = DefaultRouter()
router.register(r'user',UserApi)

urlpatterns = [
    path('',include(router.urls)),
    path('students/<int:pk>/', StudentDetailApi.as_view(), name='student-detail'),
    path("students/", StudentListApi.as_view(), name="student-list"),
    path('teachers/<int:pk>/', TeacherDetailApi.as_view(), name='teacher-detail'),
    path("teachers/", TeacherListApi.as_view(), name="teacher-list"),
    ]