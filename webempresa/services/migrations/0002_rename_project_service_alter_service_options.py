# Generated by Django 5.0.1 on 2024-02-15 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]