from rest_framework import generics
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated



class DepartemenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer

class DepartemenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartemenSerializer
    queryset = Departemen.objects.all()
    # permission_classes = [IsAuthenticated]
