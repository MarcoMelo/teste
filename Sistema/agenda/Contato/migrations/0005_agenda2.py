# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0004_auto_20150825_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='agenda2',
            fields=[
                ('agenda_id', models.AutoField(primary_key=True, serialize=False)),
                ('agenda_assunto', models.CharField(max_length=50)),
                ('agenda_descricao', models.CharField(max_length=200)),
                ('agenda_dt_cadastro', models.DateField()),
                ('agenda_dt_fim', models.DateField()),
                ('agenda_finalizado', models.BooleanField(verbose_name='finalizado?')),
            ],
        ),
    ]
