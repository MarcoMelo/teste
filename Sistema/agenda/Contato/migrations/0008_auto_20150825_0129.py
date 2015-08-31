# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0007_auto_20150825_0126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='agenda2',
            new_name='agenda',
        ),
    ]
