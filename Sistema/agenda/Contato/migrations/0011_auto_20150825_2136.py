# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0010_carro_documentos_seto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='seto',
            new_name='setor',
        ),
    ]
