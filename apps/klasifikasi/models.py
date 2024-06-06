from django.db import models

class Klasifikasi(models.Model):
    kode = models.CharField(max_length=100, unique=True)
    deskripsi = models.CharField(max_length=100)
    organisasi = models.CharField(max_length=100)

    def __str__(self):
        return self.kode

