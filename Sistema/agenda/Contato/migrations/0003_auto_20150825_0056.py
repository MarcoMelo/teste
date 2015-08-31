# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0002_auto_20150825_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='contato_ativo',
            field=models.BooleanField(verbose_name='ativo'),
        ),
    ]
