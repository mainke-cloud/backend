from django.db import models
from apps.departemen.models import Departemen
from apps.jabatan.models import Jabatan
from django.contrib.auth.models import User

class Sekretaris(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True, default=None)
    sifat = models.CharField(max_length=50, null=True, default=None)
    hak_sekretaris = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return f"{self.user.profile.nama_lengkap} ({self.status})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=50, default="-")
    departemen = models.ForeignKey(Departemen, on_delete=models.CASCADE, related_name='departemen_user', null=True, default=None)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, related_name='jabatan_user', null=True, default=None)
    alamat = models.CharField(max_length=100, default="-")
    kota = models.CharField(max_length=50, default="-")
    phone_number = models.CharField(max_length=15, default="-")
    nik_group = models.CharField(max_length=20, default="-")
    nik_lokal = models.CharField(max_length=20, default="-")
    organisasi = models.CharField(max_length=100, default="-")
    is_first_login = models.BooleanField(default=True)
    sekretaris = models.ManyToManyField(Sekretaris, blank=True, symmetrical=False, related_name='sekretaris_karyawan')

    def __str__(self):
        return f"{self.nama_lengkap}" 

