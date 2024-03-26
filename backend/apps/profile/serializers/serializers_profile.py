from rest_framework import serializers
from apps.profile.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','date_joined','last_login']
        extra_kwargs = {'email': {'read_only': True},
                    'date_joined': {'read_only': True},
                    'last_login': {'read_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    alamat = serializers.CharField(source='profile.alamat', read_only=True)
    kota = serializers.CharField(source='profile.kota', read_only=True)
    phone_number = serializers.CharField(source='profile.phone_number', read_only=True)
    nik_group = serializers.CharField(source='profile.nik_group', read_only=True)
    nik_lokal = serializers.CharField(source='profile.nik_lokal', read_only=True)
    organisasi = serializers.CharField(source='profile.organisasi', read_only=True)
    nama_lengkap = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()


    def get_nama_lengkap(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_email(self, obj):
        return f"{obj.email}"
        
    class Meta:
        model = Profile
        fields = ['id', 'nama_lengkap', 'alamat', 'email', 'kota', 'phone_number', 'nik_group', 'nik_lokal', 'organisasi']
        # extra_kwargs = {'user': {'write_only': True}}

    def create(self, validated_data):
        user = validated_data.pop('user', None)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        user = validated_data.pop('user', None)
        if user:
            instance.user = user
        instance.nama_lengkap = validated_data.get('nama_lengkap', instance.nama_lengkap)
        instance.save()
        return instance




