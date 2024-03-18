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
    detail_user = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Profile
        fields = ['id','detail_user','user','nama_lengkap','alamat','email','kota','phone_number','nik_group','nik_lokal','organisasi']
        extra_kwargs = {'user': {'write_only': True}}

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




