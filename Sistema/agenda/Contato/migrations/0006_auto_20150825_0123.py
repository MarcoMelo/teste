# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0005_agenda2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda2',
            name='agenda_descricao',
            field=models.TextField(),
        ),
    ]
