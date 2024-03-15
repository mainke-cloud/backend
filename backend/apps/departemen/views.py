from rest_framework import generics
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists

class DepartemenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]

class DepartemenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]
