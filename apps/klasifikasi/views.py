from rest_framework import generics
from apps.klasifikasi.models import Klasifikasi
from apps.klasifikasi.serializers import KlasifikasiSerializer
from rest_framework.permissions import IsAuthenticated

class KlasifikasiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Klasifikasi.objects.all()
    serializer_class = KlasifikasiSerializer
    # permission_classes = [IsAuthenticated]

class KlasifikasiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klasifikasi.objects.all()
    serializer_class = KlasifikasiSerializer
    # permission_classes = [IsAuthenticated]
