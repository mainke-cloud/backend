from rest_framework import serializers
from .models import Surat, Disposisi
from django.contrib.auth.models import User
from apps.profile.serializers.serializers_profile import UserSerializer
# class SuratSerializer(serializers.ModelSerializer): 
#     pengirim = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    

#     class Meta:
#         model = Surat 
#         fields = ['id_surat','pengirim','penerima','no_agenda', 'no_surat', 'perihal', 'status', 'urgensi', 'tanggal_pengiriman', 'id_lampiran']

#     def create(self, validated_data):
#         #user = self.context.get('user')
#         surat = Surat.objects.create(
#             pengirim = validated_data["pengirim"],
#             no_agenda = validated_data["no_agenda"],
#             no_surat = validated_data["no_surat"], 
#             perihal = validated_data["perihal"],
#             status = validated_data["status"],
#             urgensi = validated_data["urgensi"], 
#             tanggal_pengiriman = validated_data["tanggal_pengiriman"],
#             id_lampiran = validated_data["id_lampiran"])

#         surat.save()

#         for penerima in validated_data['penerima']:
#             surat.penerima.add(penerima)

#         return surat
    
#     def update(self, instance, validated_data):
#         instance.no_agenda = validated_data['no_agenda']
#         instance.no_surat = validated_data['no_surat']
#         instance.perihal = validated_data['perihal']
#         instance.status = validated_data['status']
#         instance.urgensi = validated_data['urgensi']
#         instance.tanggal_pengiriman = validated_data['tanggal_pengiriman']
#         instance.id_lampiran = validated_data['id_lampiran']
#         instance.penerima.clear()
        
#         for penerima in validated_data['penerima']:
#             instance.penerima.add(penerima)
#         instance.save()

#         return instance

class LogSerializer(serializers.Serializer):
    aksi = serializers.CharField()
    oleh = serializers.CharField()
    tanggal = serializers.CharField()

class SuratSerializer(serializers.ModelSerializer):
    log = LogSerializer(many=True)
    penerima = UserSerializer(many=True)

    class Meta:
        model = Surat
        fields = ['id_surat', 'penerima', 'no_agenda', 'no_surat', 'perihal', 'status', 'urgensi', 'tanggal_pengiriman', 'id_lampiran', 'log']

    def create(self, validated_data):
        log_data = validated_data.pop('log', [])
        
        penerima_data = validated_data.pop('penerima', [])
        surat = Surat.objects.create(**validated_data)
        for data in log_data:
            surat.log.append(data)
            print(data)
        print(surat.log)
        for data in penerima_data:
            surat.penerima.add(data)
        surat.save()
        return surat

    def update(self, instance, validated_data):
        log_data = validated_data.pop('log', [])
        instance = super().update(instance, validated_data)
        for data in log_data:
            instance.log.append(data)
        return instance

class DisposisiSerializer(serializers.ModelSerializer):
    disposisi_oleh = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Disposisi 
        fields = ['id_disposisi','disposisi_oleh','disposisi_kepada','surat', 'komentar', 'tanggal_disposisi']
    
    def create(self, validated_data):
        #user = self.context.get('user')
        disposisi = Disposisi.objects.create(disposisi_oleh = validated_data["disposisi_oleh"], surat = validated_data["surat"], komentar = validated_data["komentar"], 
                                        tanggal_disposisi = validated_data["tanggal_disposisi"])
        disposisi.save()

        for penerima in validated_data['disposisi_kepada']:
            disposisi.disposisi_kepada.add(penerima)

        return disposisi