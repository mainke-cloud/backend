from django.db import models
from apps.divisi.models import Divisi


class Departemen(models.Model):
    id_departemen = models.AutoField(primary_key=True)
    nama_departemen = models.CharField(max_length=100)
    id_divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='departemen')

    def __str__(self):
        return self.nama_departemen