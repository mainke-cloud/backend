from django.db import models
from apps.divisi.models import Divisi


class Departemen(models.Model):
    nama_departemen = models.CharField(max_length=100)
    kode_departemen = models.CharField(max_length=100)
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='divisi_departemen')

    def __str__(self):
        return self.nama_departemen