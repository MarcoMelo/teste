# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='contato_favorito',
            new_name='contato_ativo',
        ),
        migrations.AddField(
            model_name='contato',
            name='contato_cidade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contato',
            name='contato_telefone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='contato',
            name='contato_tipo_telefone',
            field=models.CharField(max_length=10, choices=[('fixo', 'Fixo'), ('celular', 'Celular')], verbose_name='TIPO TELEFONE', null=True),
        ),
    ]
