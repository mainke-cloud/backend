from django.db import models
from apps.divisi.models import Divisi
from apps.jabatan.models import Jabatan
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=50, default="-")
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='divisi_user', null=True, default=None)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, related_name='jabatan_user', null=True, default=None)
    alamat = models.CharField(max_length=100, default="-")
    kota = models.CharField(max_length=50, default="-")
    phone_number = models.CharField(max_length=15, default="-")
    nik_group = models.CharField(max_length=20, default="-")
    nik_lokal = models.CharField(max_length=20, default="-")
    organisasi = models.CharField(max_length=100, default="-")
    is_first_login = models.BooleanField(default=True)
    role = models.CharField(max_length=20, default="User")
    personal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nama_lengkap}" 

class Sekretaris(models.Model): 
    atasan = models.ForeignKey(Profile, related_name='sekretaris_atasan', on_delete=models.CASCADE)
    sekretaris = models.ForeignKey(Profile, related_name='sekretaris_bawahan', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    sifat = models.BooleanField(default=True)
    hak_sekretaris = models.CharField(max_length=50, null=True, default='Biasa')
    tgl_pembuatan = models.DateField()

    def __str__(self):
        return f"{self.sekretaris.nama_lengkap} ({self.status})"

class Delegasi(models.Model): 
    atasan = models.ForeignKey(Profile, related_name='delegasi_atasan', on_delete=models.CASCADE)
    delegasi = models.ForeignKey(Profile, related_name='delegasi_bawahan', on_delete=models.CASCADE)
    alasan = models.CharField(max_length=100, null=True, default="-")
    tgl_aktif = models.DateField()
    tgl_berakhir = models.DateField()
    disetujui = models.BooleanField(default=False)

    def status(self):
        if self.tgl_berakhir >= timezone.now().date():
            return "Aktif"
        else:
            return "Tidak Aktif"

    def __str__(self):
        return f"{self.delegasi.nama_lengkap} ({self.status()})"

