# Generated by Django 4.1.13 on 2024-04-25 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divisi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('divisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisi_group', to='divisi.divisi')),
                ('person', models.ManyToManyField(related_name='secretary_group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
