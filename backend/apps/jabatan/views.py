from rest_framework import generics
from apps.jabatan.models import Jabatan
from apps.jabatan.serializers import JabatanSerializer

class JabatanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer

class JabatanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    lookup_field = 'id_jabatan'
