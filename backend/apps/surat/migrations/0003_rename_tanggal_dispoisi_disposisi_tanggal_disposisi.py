# Generated by Django 5.0.3 on 2024-03-06 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("surat", "0002_disposisi"),
    ]

    operations = [
        migrations.RenameField(
            model_name="disposisi",
            old_name="tanggal_dispoisi",
            new_name="tanggal_disposisi",
        ),
    ]
