<<<<<<< HEAD
# Generated by Django 4.2.7 on 2023-11-17 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apiuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiuser.usuario')),
            ],
        ),
    ]
=======
# Generated by Django 4.2.7 on 2023-11-17 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apiuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiuser.usuario')),
            ],
        ),
    ]
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
