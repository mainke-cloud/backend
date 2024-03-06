from rest_framework import serializers
from .models import Divisi, Group
from django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id_group','divisi','person', 'type']
    
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