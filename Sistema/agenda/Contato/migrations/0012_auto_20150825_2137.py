# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0011_auto_20150825_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setor',
            old_name='Contato',
            new_name='Contatos',
        ),
    ]
