from rest_framework import serializers
from apps.divisi.models import Divisi
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer

class DivisiSerializer(serializers.ModelSerializer):
    departemen_detail = DepartemenSerializer(source='departemen', read_only=True)    
    class Meta:
        model = Divisi
        fields = ['id','nama_divisi','short_name','kode_divisi','departemen_detail','departemen']
        extra_kwargs = {'departemen': {'write_only': True}}

    def create(self, validated_data):
        departemen = validated_data.pop('departemen', None)
        divisi = Divisi.objects.create(departemen=departemen, **validated_data)
        return divisi

    def update(self, instance, validated_data):
        departemen = validated_data.pop('departemen', None)
        if departemen:
            instance.departemen = departemen
        instance.nama_divisi = validated_data.get('nama_divisi', instance.nama_divisi)
        instance.short_name = validated_data.get('short_name', instance.short_name)
        instance.kode_divisi = validated_data.get('kode_divisi', instance.kode_divisi)
        instance.save()
        return instance
