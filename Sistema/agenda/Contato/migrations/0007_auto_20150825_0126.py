# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0006_auto_20150825_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda2',
            name='agenda_finalizado',
            field=models.BooleanField(verbose_name='Finalizado?'),
        ),
    ]
