import jwt
from rest_framework import serializers
from django.contrib.auth.models import User
from apps.profile.models import Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterSerializer, self).__init__(*args, **kwargs)
        self.user = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password','password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError("Password confirmation does not match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserAdminRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    nama_lengkap = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    organisasi = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterSerializer, self).__init__(*args, **kwargs)
        self.user = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'nama_lengkap', 'phone_number', 'organisasi']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError("Password confirmation does not match")
        return data
    
    def create(self, validated_data):
        user_data = {
            'username': validated_data['username'],
            'email': validated_data['email'],
            'password': validated_data['password']
        }

        # Create the user
        user = User.objects.create_user(**user_data)

        # Create the profile
        profile_data = {
            'user': user,
            'nama_lengkap': validated_data['nama_lengkap'],
            'phone_number': validated_data['phone_number'],
            'organisasi': validated_data['organisasi'],
            'role': "Admin"
        }
        Profile.objects.create(**profile_data)

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']