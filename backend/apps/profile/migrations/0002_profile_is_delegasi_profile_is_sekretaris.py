# Generated by Django 4.1.13 on 2024-05-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_delegasi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_sekretaris',
            field=models.BooleanField(default=False),
        ),
    ]
