# from django.core.cache import cache
# from rest_framework.decorators import api_view
# from rest_framework.exceptions import PermissionDenied
# from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from rest_framework.permission import IsPhoneVerified
# from .serializers import *
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import viewsets, generics, permissions
#
#
#
#
# class SendSmsAPIView(APIView):
#     @swagger_auto_schema(request_body=SendSmsSerializer)
#     def post(self, request):
#         serializer = SendSmsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         phone_number = serializer.validated_data['phone_number']
#         sms_kod = str(random.randint(1000, 9999))
#         print(f"SMS kod {phone_number} --> {sms_kod}")
#         if sms_kod:
#             cache.set(phone_number,sms_kod,600)
#         return Response({'SMS kod yuborildi (terminalga print)'})