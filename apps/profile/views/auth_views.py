from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from apps.profile.serializers.serializers_auth import *
from apps.profile.serializers.serializers_profile import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt
from datetime import datetime as dtime, timedelta
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        user = User.objects.filter(username=username).first()
        if user :
            raise AuthenticationFailed('User is already!')

        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterAdminView(APIView):
    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        if user :
            raise AuthenticationFailed('User is already!')

        serializer = UserAdminRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        # Mengatur waktu kedaluwarsa access token menjadi 3 hari dari sekarang
        access_token.set_exp(lifetime=timedelta(days=3))

        # Mengatur waktu kedaluwarsa refresh token jika diperlukan
        refresh.set_exp(lifetime=timedelta(days=3))  # Misalnya 3 hari

        # Mendapatkan waktu expired dari access token
        access_token_exp = dtime.fromtimestamp(access_token['exp'])

        # Mendapatkan waktu expired dari refresh token
        refresh_token_exp = dtime.fromtimestamp(refresh['exp'])
        
        if user and user.check_password(password):
            response = Response({
                'id': user.id,
                'username': username,
                'jwt': str(access_token),
                'access_token_exp': access_token_exp,
                'refresh_token_exp': refresh_token_exp,
                'message': "Succes Login!",
            })
            
            return response
        else:
            return Response({'message': 'Invalid credentials'}, status=400)