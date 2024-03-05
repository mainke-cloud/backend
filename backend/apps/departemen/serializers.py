from rest_framework import serializers
from apps.departemen.models import Departemen
from apps.divisi.serializers import DivisiSerializer

class DepartemenSerializer(serializers.ModelSerializer):
    divisi = DivisiSerializer(source='id_divisi')

    class Meta:
        model = Departemen
        fields = ['id_departemen','divisi','nama_departemen']