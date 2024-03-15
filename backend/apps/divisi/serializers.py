from rest_framework import serializers
from apps.divisi.models import Divisi

class DivisiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Divisi
        fields = ['id','nama_divisi']

    def create(self, validated_data):
        return Divisi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nama_divisi = validated_data.get('nama_divisi', instance.nama_divisi)
        instance.save()
        return instance
