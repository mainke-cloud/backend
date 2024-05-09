from rest_framework import serializers
from apps.profile.models import *
from django.contrib.auth.models import User
from apps.departemen.models import Departemen
from apps.jabatan.models import Jabatan
from apps.departemen.serializers import DepartemenSerializer
from apps.jabatan.serializers import JabatanSerializer

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = ['user_id','username','nama_lengkap']
        extra_kwargs = {'user': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user',read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', required=False)
    departemen_detail = DepartemenSerializer(source='departemen', read_only=True)
    jabatan_detail = JabatanSerializer(source='jabatan', read_only=True)
    my_sekretaris = serializers.SerializerMethodField()
        
    class Meta:
        model = Profile
        fields = ['user_id','username','email','nama_lengkap','departemen_detail','jabatan_detail','alamat','kota', 'phone_number', 'nik_group', 'nik_lokal', 'organisasi','is_first_login','departemen','jabatan','nama_lengkap','my_sekretaris']
        extra_kwargs = {
        'departemen': {'write_only': True},
        'jabatan': {'write_only': True},
        'user': {'write_only': True},
        'sekretaris': {'write_only': True},
        }
    
    def get_my_sekretaris(self, obj):
        sekretaris = Sekretaris.objects.filter(atasan=obj)
        return SekretarisSerializer(sekretaris, many=True).data

    def create(self, validated_data):    
        user = validated_data.pop('user', None)
        id_user = self.context['request'].query_params.get('id_user')
        user_data = User.objects.get(id=id_user)
        
        email = self.context['request'].data.get('email', []) 
        if email:  
            user_data.email = email
            user_data.save()
        profile = Profile.objects.create(user=user_data, **validated_data)
        return profile


    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        id_user = self.context['request'].query_params.get('id_user')
        if user_data:
            user = instance.user
            email = user_data.get('email', None)
            if email is not None and email != user.email:
                user.email = email
                user.save()

        # Update departemen, jabatan
        instance.departemen = validated_data.get('departemen', instance.departemen)
        instance.jabatan = validated_data.get('jabatan', instance.jabatan)
        # Update field lainnya
        instance.alamat = validated_data.get('alamat', instance.alamat)
        instance.kota = validated_data.get('kota', instance.kota)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.nik_group = validated_data.get('nik_group', instance.nik_group)
        instance.nik_lokal = validated_data.get('nik_lokal', instance.nik_lokal)
        instance.organisasi = validated_data.get('organisasi', instance.organisasi)
        instance.nama_lengkap = validated_data.get('nama_lengkap', instance.nama_lengkap)
        instance.is_first_login = validated_data.get('is_first_login', instance.is_first_login)

        instance.save()
        return instance


class SekretarisSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='sekretaris.user', queryset=User.objects.all())
    username = serializers.ReadOnlyField(source='sekretaris.user.username')
    nama_lengkap = serializers.ReadOnlyField(source='sekretaris.nama_lengkap')
    class Meta:
        model = Sekretaris
        fields = ('user_id','username','nama_lengkap','status', 'sifat', 'hak_sekretaris')

    def create(self, validated_data):
        id_user = self.context['request'].query_params.get('id_user')
        atasan = Profile.objects.get(user_id=id_user)
        sekretaris = validated_data.pop('sekretaris', None)
        sekretaris_obj = Profile.objects.get(user_id=sekretaris['user'].id)
        sekretaris_instance = Sekretaris.objects.create(atasan=atasan, sekretaris=sekretaris_obj, **validated_data)
        return sekretaris_instance

    def update(self, instance, validated_data):
        try:
            print("instance1:",instance)
            print("validated_data:",validated_data)
            instance.status = validated_data['status']
            instance.sifat = validated_data['sifat']
            instance.hak_sekretaris = validated_data['hak_sekretaris']
            print("instance2:",instance)
            instance.save()
            return instance
        except KeyError as e:
            raise ValidationError(str(e))