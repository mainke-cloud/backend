from rest_framework import generics
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


class DivisiListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DivisiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_departemen = self.request.query_params.get('id_departemen')
        queryset = Divisi.objects.all()
        if id_departemen :
            queryset = queryset.filter(departemen_id = id_departemen)
        if not queryset:
            raise NotFound("Divisi not found!")
        return queryset

class DivisiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    permission_classes = [IsAuthenticated]
