from rest_framework import serializers
from apps.departemen.models import Departemen
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer

class DepartemenSerializer(serializers.ModelSerializer):
    divisi_detail = DivisiSerializer(source='divisi', read_only=True)

    class Meta:
        model = Departemen
        fields = ['id', 'nama_departemen','kode_departemen','divisi_detail','divisi']
        extra_kwargs = {'divisi': {'write_only': True}}

    def create(self, validated_data):
        divisi = validated_data.pop('divisi', None)
        departemen = Departemen.objects.create(divisi=divisi, **validated_data)
        return departemen

    def update(self, instance, validated_data):
        divisi = validated_data.pop('divisi', None)
        if divisi:
            instance.divisi = divisi
        instance.nama_departemen = validated_data.get('nama_departemen', instance.nama_departemen)
        instance.kode_departemen = validated_data.get('kode_departemen', instance.kode_departemen)
        instance.save()
        return instance