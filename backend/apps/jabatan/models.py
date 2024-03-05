from django.db import models

class Jabatan(models.Model):
    id_jabatan = models.AutoField(primary_key=True)
    nama_jabatan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_jabatan
