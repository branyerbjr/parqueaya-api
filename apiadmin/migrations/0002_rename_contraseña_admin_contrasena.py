# Generated by Django 4.2.7 on 2023-12-17 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
