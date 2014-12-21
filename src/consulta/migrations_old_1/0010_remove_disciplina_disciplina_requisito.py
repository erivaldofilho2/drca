# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0009_disciplina_disciplina_requisito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='disciplina_requisito',
        ),
    ]
