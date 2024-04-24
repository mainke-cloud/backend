from rest_framework import serializers
from apps.profile.models import Profile
from django.contrib.auth.models import User
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','date_joined','last_login']
        extra_kwargs = {'username': {'read_only': True},
                    'date_joined': {'read_only': True},
                    'last_login': {'read_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user',read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', required=False)
    departemen_detail = DepartemenSerializer(source='departemen', read_only=True)
    
    # def get_user(self, obj):
    #     logged_user = self.context['request'].COOKIES.get('id')
    #     user = User.objects.get(pk=logged_user)
    #     return user
        
    class Meta:
        model = Profile
        fields = ['user_id','username','email','nama_lengkap','departemen_detail','alamat','kota', 'phone_number', 'nik_group', 'nik_lokal', 'organisasi','is_first_login','departemen','nama_lengkap']
        extra_kwargs = {
        'departemen': {'write_only': True},
        'user': {'write_only': True},
        }
    
    def create(self, validated_data):
        email = validated_data.pop('email', None)
        id_user = self.context['request'].query_params.get('id_user')
        user_data = User.objects.get(id = id_user)
        profile = Profile.objects.create(user = user_data, **validated_data)
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            email = user_data.get('email', None)
            if email is not None and email != user.email:
                # Periksa apakah alamat email telah diubah
                user.email = email
                user.save()

        instance.alamat = validated_data.get('alamat', instance.alamat)
        instance.kota = validated_data.get('kota', instance.kota)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.nik_group = validated_data.get('nik_group', instance.nik_group)
        instance.nik_lokal = validated_data.get('nik_lokal', instance.nik_lokal)
        instance.organisasi = validated_data.get('organisasi', instance.organisasi)
        instance.departemen = validated_data.get('departemen', instance.departemen)
        instance.nama_lengkap = validated_data.get('nama_lengkap', instance.nama_lengkap)
        instance.is_first_login = validated_data.get('is_first_login', instance.is_first_login)


        instance.save()
        return instance




