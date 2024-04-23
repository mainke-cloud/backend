from rest_framework import generics
from apps.profile.models import Profile
from apps.profile.serializers.serializers_profile import *
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists
from rest_framework.response import Response
from django.contrib.auth.models import User


class ProfileAPIView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        logged_user = self.request.COOKIES.get('email')
        profile = Profile.objects.get(user__email=logged_user)
        return profile
    
    def get(self, request):
        logged_user = request.COOKIES.get('id')
        print(logged_user)
        user_profile = User.objects.get(id=logged_user)
        print(user_profile)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data)
    
    def post(self, request):   
        serializer = ProfileSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        logged_user = self.request.COOKIES.get('email')
        profile = Profile.objects.get(user__email=logged_user)
        return profile

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)