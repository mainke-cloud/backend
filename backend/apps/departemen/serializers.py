from rest_framework import serializers
from apps.departemen.models import Departemen
from apps.divisi.serializers import DivisiSerializer

class DepartemenSerializer(serializers.ModelSerializer):
    divisi = DivisiSerializer(source='id_divisi', read_only=True)

    class Meta:
        model = Departemen
        fields = ['id_departemen','id_divisi','divisi','nama_departemen']
        extra_kwargs = {'id_divisi': {'write_only': True}}