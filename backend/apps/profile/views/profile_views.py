from rest_framework import generics
from apps.profile.models import Profile
from apps.profile.serializers.serializers_profile import *
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists
from rest_framework.response import Response


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]

    def get(self, request):
        logged_user = request.COOKIES.get('email')
        print(request.COOKIES.get('email'))
        user_profile = Profile.objects.get(email=logged_user)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data)

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # lookup_field = 'id_profile'
    permission_classes = [IsAuthenticatedAndTokenExists] 

    def get(self, request):
        logged_user = request.COOKIES.get('email')
        print(request.COOKIES.get('email'))
        user_profile = Profile.objects.get(email=logged_user)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data)