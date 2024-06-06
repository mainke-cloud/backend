from rest_framework import serializers
from apps.klasifikasi.models import Klasifikasi

class KlasifikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klasifikasi
        fields = ['id','kode','deskripsi','organisasi']

    def create(self, validated_data):
        return Klasifikasi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.kode = validated_data.get('kode', instance.kode)
        instance.deskripsi = validated_data.get('deskripsi', instance.deskripsi)
        instance.organisasi = validated_data.get('organisasi', instance.organisasi)
        instance.save()
        return instance
