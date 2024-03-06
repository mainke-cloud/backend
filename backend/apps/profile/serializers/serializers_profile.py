from rest_framework import serializers
from apps.profile.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','date_joined','last_login']
        extra_kwargs = {'username': {'read_only': True},
                    'date_joined': {'read_only': True},
                    'last_login': {'read_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='id_user', read_only=True)
    class Meta:
        model = Profile
        fields = ['id_profile','id_user','user','nama_lengkap','alamat','email','kota','phone_number','nik_group','nik_lokal','organisasi']
        extra_kwargs = {'id_user': {'write_only': True}}




