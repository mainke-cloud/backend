from rest_framework import serializers
from apps.departemen.models import Departemen

class DepartemenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departemen
        fields = ['id', 'nama_departemen','kode_departemen','short_name']
        extra_kwargs = {'divisi': {'write_only': True}}

    def create(self, validated_data):        
        return Departemen.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nama_departemen = validated_data.get('nama_departemen', instance.nama_departemen)
        instance.kode_departemen = validated_data.get('kode_departemen', instance.kode_departemen)
        instance.short_name = validated_data.get('short_name', instance.short_name)
        instance.save()
        return instance