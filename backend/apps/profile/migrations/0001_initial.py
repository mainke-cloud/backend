# Generated by Django 5.0.3 on 2024-03-05 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id_profile', models.AutoField(primary_key=True, serialize=False)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('kota', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('nik_group', models.CharField(max_length=20)),
                ('nik_lokal', models.CharField(max_length=20)),
                ('organisasi', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]