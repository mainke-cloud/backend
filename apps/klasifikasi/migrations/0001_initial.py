# Generated by Django 4.1.13 on 2024-06-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klasifikasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=100, unique=True)),
                ('deskripsi', models.CharField(max_length=100)),
                ('organisasi', models.CharField(max_length=100)),
            ],
        ),
    ]
