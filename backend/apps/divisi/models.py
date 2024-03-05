from django.db import models

class Divisi(models.Model):
    id_divisi = models.AutoField(primary_key=True)
    nama_divisi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_divisi
