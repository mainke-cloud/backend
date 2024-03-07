from rest_framework import generics
from apps.profile.models import Profile
from apps.profile.serializers.serializers_profile import *
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # lookup_field = 'id_profile'
    permission_classes = [IsAuthenticatedAndTokenExists]
