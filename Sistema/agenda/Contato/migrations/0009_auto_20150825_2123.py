# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0008_auto_20150825_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='contato_tipo_telefone',
            field=models.CharField(max_length=10, null=True, verbose_name='Tipo Telefone', choices=[('fixo', 'Fixo'), ('celular', 'Celular')]),
        ),
    ]
