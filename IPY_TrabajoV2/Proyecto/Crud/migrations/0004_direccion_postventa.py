# Generated by Django 3.2 on 2021-07-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0003_auto_20210618_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postventa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(default='NOMBRE COMPLETO', max_length=100)),
                ('rut', models.CharField(default='RUT', max_length=11)),
                ('direccion', models.CharField(default='DIRECCION', max_length=100)),
                ('postventa', models.CharField(default='NUMERO POSTVENTA', max_length=11)),
                ('tipo_postventa', models.CharField(default='TIPO POSTVENTA', max_length=100)),
                ('conductor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Crud.conductor')),
                ('estado_compra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Crud.estadocompra')),
            ],
        ),
    ]
