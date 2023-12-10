# Generated by Django 4.2.7 on 2023-12-10 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apiadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_metodo_pago', models.CharField(max_length=255)),
                ('datos_metodo_pago', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiadmin.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tarifa', models.CharField(max_length=255)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.metodopago')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiadmin.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroPagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_pago', models.CharField(max_length=255)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('transaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.transaccion')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('transaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.transaccion')),
            ],
        ),
    ]
