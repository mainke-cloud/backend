from rest_framework import generics
from apps.profile.models import Profile
from apps.profile.serializers.serializers_profile import *
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists
from rest_framework.response import Response
from django.contrib.auth.models import User


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        id_jabatan = self.request.query_params.get('id_jabatan')
        id_departemen = self.request.query_params.get('id_departemen')
        queryset = Profile.objects.all()
        if id_user :
            queryset = queryset.filter(user_id = id_user)
        elif id_departemen :
            queryset = queryset.filter(departemen_id = id_departemen)
        elif id_jabatan :
            queryset = queryset.filter(jabatan_id = id_jabatan)
        return queryset


    # def get_object(self):
    #     logged_user = self.request.COOKIES.get('id')
    #     profile = Profile.objects.get(user__id=logged_user)
    #     return profile
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfileUpdateRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'
    
    def get_queryset(self):
        id = self.kwargs[self.lookup_field]
        queryset = Profile.objects.filter(user_id = id)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    # def get_object(self):
    #     logged_user = self.request.COOKIES.get('id')
    #     profile = Profile.objects.get(user__id=logged_user)
    #     return profile

    # def update(self, request, *args, **kwargs):
    #     profile = self.get_object()
    #     serializer = ProfileSerializer(profile, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)