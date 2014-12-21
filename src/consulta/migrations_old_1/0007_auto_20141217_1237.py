# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0006_auto_20141217_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplina',
            old_name='disciplina_pre',
            new_name='disciplina_requisito',
        ),
    ]
