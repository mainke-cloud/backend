# Generated by Django 4.1.13 on 2024-05-09 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surat',
            name='prioritas_surat',
        ),
    ]