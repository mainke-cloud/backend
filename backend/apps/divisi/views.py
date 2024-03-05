from rest_framework import generics
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer

class DivisiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer

class DivisiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    lookup_field = 'id_divisi'
