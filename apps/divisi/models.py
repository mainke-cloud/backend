from django.db import models
from apps.departemen.models import Departemen

class Divisi(models.Model):
    nama_divisi = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    kode_divisi = models.CharField(max_length=100)
    departemen = models.ForeignKey(Departemen, on_delete=models.CASCADE, related_name='departemen_divisi')
 
    def __str__(self):
        return self.nama_divisi
