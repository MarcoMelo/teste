# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0009_auto_20150825_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='carro',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('Contato', models.ForeignKey(to='Contato.Contato')),
            ],
        ),
        migrations.CreateModel(
            name='documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rg', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=11)),
                ('Contato', models.OneToOneField(to='Contato.Contato')),
            ],
        ),
        migrations.CreateModel(
            name='seto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=40)),
                ('Contato', models.ManyToManyField(to='Contato.Contato')),
            ],
        ),
    ]
