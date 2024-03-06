from django.db import models
from apps.divisi.models import Divisi
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model): 
    id_group = models.AutoField(primary_key=True)
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='divisi_group')
    person = models.ManyToManyField(User, related_name='secretary_group')
    type = models.IntegerField()
    