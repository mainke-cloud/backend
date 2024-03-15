# Generated by Django 4.1.13 on 2024-03-15 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('kota', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('nik_group', models.CharField(max_length=20)),
                ('nik_lokal', models.CharField(max_length=20)),
                ('organisasi', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
