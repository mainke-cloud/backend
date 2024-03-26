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
    user_id = serializers.PrimaryKeyRelatedField(source='user',read_only=True)    
    nama_lengkap = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)

    def get_nama_lengkap(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_email(self, obj):
        return f"{obj.user.email}"
        
    class Meta:
        model = Profile
        fields = ['user_id','nama_lengkap', 'alamat', 'email', 'kota', 'phone_number', 'nik_group', 'nik_lokal', 'organisasi']
    
    def create(self, validated_data):
        logged_user = self.context['request'].COOKIES.get('email')
        user = User.objects.get(email=logged_user)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        user = validated_data.pop('user', None)
        if user:
            instance.user = user
        instance.alamat = validated_data.get('alamat', instance.alamat)
        instance.kota = validated_data.get('kota', instance.kota)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.nik_group = validated_data.get('nik_group', instance.nik_group)
        instance.nik_lokal = validated_data.get('nik_lokal', instance.nik_lokal)
        instance.organisasi = validated_data.get('organisasi', instance.organisasi)
        instance.save()
        return instance




