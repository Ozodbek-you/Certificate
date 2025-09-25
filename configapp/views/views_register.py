import random
from django.contrib.auth.hashers import make_password
from configapp.Permission import IsEmailVerified, IsAdmin
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from configapp.serializers import SendEmail,VerifySerializer,UserSerializer

import random

from django.contrib.auth.hashers import make_password
from configapp.Permission import IsAdmin,IsStudentPermission
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from configapp.serializers import SendEmail,VerifySerializer
class SendEmailAPI(APIView):
    permission_classes = [IsAdmin]
    @swagger_auto_schema(request_body=SendEmail)
    def post(self, request):
        user = request.user
        serializer = SendEmail(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = "Ro'yxatdan o'tish kodi"
        otp_code = str(random.randint(100000, 999999))
        email = serializer.validated_data['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        password = str(random.randint(1000, 9999))
        cache.set(f"{email}_otp", otp_code, 600)
        message = f"""
        Sizning tasdiqlash kodingiz: {otp_code}
        Vaqtinchalik parolingiz: {password}
        """
        user.password = make_password(password)

        send_mail(subject, message, email_from, recipient_list)
        return Response(data={f"{email}": "OTP va parol yuborildi"})
#             return Response({
#                 'status': False,
#                 'detail': 'In Correct'
#             })
