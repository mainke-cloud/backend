from rest_framework import generics
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer

class DepartemenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer

class DepartemenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer
    lookup_field = 'id_departemen'
