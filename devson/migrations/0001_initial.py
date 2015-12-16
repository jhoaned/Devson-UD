# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2015-12-16 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstiloObjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('V_TipoLetra', models.CharField(max_length=100)),
                ('V_Color', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('V_CoordenadaX', models.IntegerField()),
                ('V_CoordenadaY', models.IntegerField()),
                ('N_ClaseObjeto', models.CharField(max_length=4)),
                ('N_SiRaiz', models.BooleanField()),
                ('K_HijoDe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devson.Objeto')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_NombreProyecto', models.CharField(max_length=200)),
                ('V_FechaCreacion', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='TipoObjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_TipoObjeto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ValorObjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('K_ValorObjeto', models.CharField(max_length=1000)),
                ('K_Objeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devson.Objeto')),
            ],
        ),
        migrations.AddField(
            model_name='objeto',
            name='K_Proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devson.Proyecto'),
        ),
        migrations.AddField(
            model_name='objeto',
            name='K_TipoObjeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devson.TipoObjeto'),
        ),
        migrations.AddField(
            model_name='estiloobjeto',
            name='K_Objeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devson.Objeto'),
        ),
    ]
