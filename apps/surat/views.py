from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Surat, Disposisi
from .serializers import SuratSerializer, DisposisiSerializer
from rest_framework.permissions import IsAuthenticated

class SuratListCreateView(generics.ListCreateAPIView):
    queryset = Surat.objects.all()
    serializer_class = SuratSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs): 
        #user = request.user
        #serializer = self.get_serializer(data= request.data, context={'user':user})
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Surat.objects.all()
        status = self.request.query_params.get('status', None)
        kategori = self.request.query_params.get('kategori', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        if kategori is not None:
            queryset = queryset.filter(kategori=kategori)
        return queryset
    
class SuratRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Surat.objects.all()
    serializer_class = SuratSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DisposisiListCreateView(generics.ListCreateAPIView):
    queryset = Disposisi.objects.all()
    serializer_class = DisposisiSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        #user = request.user
        #serializer = self.get_serializer(data= request.data, context={'user':user})
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        return Response(serializer.data)
    
class DisposisiRetrieve(generics.RetrieveAPIView):
    queryset = Disposisi.objects.all()
    serializer_class = DisposisiSerializer