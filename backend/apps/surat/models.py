from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from apps.lampiran.models import Lampiran

class Surat(models.Model):
    penerima = models.ManyToManyField(User, related_name='penerima_surat')
    no_agenda = models.CharField(max_length=100)
    no_surat = models.CharField(max_length=100)
    perihal = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    urgensi = models.CharField(max_length=100)
    tanggal_pengiriman = models.DateField()
    lampiran = models.ForeignKey(Lampiran, on_delete=models.CASCADE, related_name='lampiran_surat')
    log = models.JSONField(default=list)

    def __str__(self):
        return self.perihal
 
class Disposisi(models.Model): 
    disposisi_oleh = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disposisi_oleh')
    disposisi_kepada = models.ManyToManyField(User, related_name='disposisi_kepada')
    surat = models.ForeignKey(Lampiran, on_delete=models.CASCADE, related_name='surat')
    komentar = models.CharField(max_length=100)
    tanggal_disposisi = models.DateField() 
    