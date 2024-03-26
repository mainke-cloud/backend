from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.CharField(max_length=100)
    kota = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    nik_group = models.CharField(max_length=20)
    nik_lokal = models.CharField(max_length=20)
    organisasi = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name