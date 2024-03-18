from rest_framework import serializers
from .models import Divisi, Group
from django.contrib.auth.models import User
from apps.profile.serializers.serializers_profile import UserSerializer
from apps.divisi.serializers import DivisiSerializer

class GroupSerializer(serializers.ModelSerializer):
    person_detail = UserSerializer(source='person', read_only=True,many=True)
    divisi_detail = DivisiSerializer(source='divisi', read_only=True)


    class Meta:
        model = Group
        fields = ['id','divisi','divisi_detail','person', 'type','person_detail']
        extra_kwargs = {'person': {'write_only': True},
                        'divisi': {'write_only': True}}

    
    def create(self, validated_data):
        #user = self.context.get('user')
        group = Group.objects.create(divisi = validated_data["divisi"], type = validated_data["type"])
        group.save()

        for p in validated_data['person']:
            group.person.add(p)

        return group

    def update(self, instance, validated_data):
        instance.divisi = validated_data['divisi']
        instance.type = validated_data['type']
        instance.person.clear()
        
        for p in validated_data['person']:
            instance.person.add(p)
        instance.save()

        return instance