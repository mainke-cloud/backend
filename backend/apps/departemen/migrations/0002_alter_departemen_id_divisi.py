# Generated by Django 5.0.3 on 2024-03-05 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departemen', '0001_initial'),
        ('divisi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departemen',
            name='id_divisi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departemen', to='divisi.divisi'),
        ),
    ]
