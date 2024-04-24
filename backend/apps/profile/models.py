from django.db import models
from apps.departemen.models import Departemen
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=50, default="-")
    email = models.EmailField()
    departemen = models.ForeignKey(Departemen, on_delete=models.CASCADE, related_name='departemen_user', null=True, default=None)
    alamat = models.CharField(max_length=100, default="-")
    kota = models.CharField(max_length=50, default="-")
    phone_number = models.CharField(max_length=15, default="-")
    nik_group = models.CharField(max_length=20, default="-")
    nik_lokal = models.CharField(max_length=20, default="-")
    organisasi = models.CharField(max_length=100, default="-")
    is_first_login = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nama_lengkap}" 