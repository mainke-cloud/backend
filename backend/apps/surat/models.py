from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from apps.lampiran.models import Lampiran

class Surat(models.Model):
    penerima = models.ManyToManyField(User, related_name='penerima_surat')
    pembuat = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pembuat_surat')
    # sequence = models.PositiveIntegerField()
    no_agenda = models.CharField(max_length=100)
    no_surat = models.CharField(max_length=100)
    perihal = models.CharField(max_length=100)
    jenis_surat = models.CharField(max_length=100,)
    prioritas_surat = models.CharField(max_length=100)
    komentar_surat = models.JSONField(default=list)
    file_surat = models.FileField(upload_to='event_files/')
    tembusan = models.ManyToManyField(User, related_name='tembusan_surat')
    referensi = models.ForeignKey(Lampiran, on_delete=models.CASCADE, related_name='referensi_surat')
    lampiran = models.ForeignKey(Lampiran, on_delete=models.CASCADE, related_name='lampiran_surat')
    status = models.CharField(max_length=100)
    urgensi = models.CharField(max_length=100)  
    tanggal_pengiriman = models.DateField()  
    log = models.JSONField(default=list)

    def __str__(self):
        return self.perihal

    def is_approved(self):
        return self.approvals.count() == self.approver.count()

    def save(self, *args, **kwargs):
        if not self.sequence:
            last_surat = Surat.objects.order_by('-sequence').first()
            if last_surat:
                self.sequence = last_surat.sequence + 1
            else:
                self.sequence = 1
        super().save(*args, **kwargs)

class Approval(models.Model):
    surat = models.ForeignKey('Surat', on_delete=models.CASCADE, related_name='surat_approvals')
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approvals')
    approved_at = models.DateTimeField(auto_now_add=True)

class Disposisi(models.Model): 
    disposisi_oleh = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disposisi_oleh')
    disposisi_kepada = models.ManyToManyField(User, related_name='disposisi_kepada')
    surat = models.ForeignKey(Surat, on_delete=models.CASCADE, related_name='surat')
    komentar = models.CharField(max_length=100)
    tanggal_disposisi = models.DateField()
    