from rest_framework.routers import DefaultRouter
from configapp.views import *
from django.urls import path, include

from configapp.views import *

router = DefaultRouter()
router.register(r'teacher',TeacherCreateApi)

urlpatterns = [
    path('',include(router.urls)),
    path('send_email/',SendEmailApi.as_view(), name = 'send_email'),
    path('verify/',VerifyApi.as_view()),
    path('register/',RegisterApi.as_view()),
]


