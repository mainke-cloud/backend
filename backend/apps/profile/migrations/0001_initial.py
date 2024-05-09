# Generated by Django 4.1.13 on 2024-05-09 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jabatan', '0001_initial'),
        ('departemen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(default='-', max_length=50)),
                ('alamat', models.CharField(default='-', max_length=100)),
                ('kota', models.CharField(default='-', max_length=50)),
                ('phone_number', models.CharField(default='-', max_length=15)),
                ('nik_group', models.CharField(default='-', max_length=20)),
                ('nik_lokal', models.CharField(default='-', max_length=20)),
                ('organisasi', models.CharField(default='-', max_length=100)),
                ('is_first_login', models.BooleanField(default=True)),
                ('departemen', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departemen_user', to='departemen.departemen')),
                ('jabatan', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jabatan_user', to='jabatan.jabatan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sekretaris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=None, max_length=50, null=True)),
                ('sifat', models.CharField(default=None, max_length=50, null=True)),
                ('hak_sekretaris', models.CharField(default=None, max_length=50, null=True)),
                ('atasan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sekretaris_atasan', to='profile.profile')),
                ('sekretaris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sekretaris_bawahan', to='profile.profile')),
            ],
        ),
    ]
