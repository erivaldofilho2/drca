# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0005_auto_20141217_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='disciplina_pre',
            field=models.ForeignKey(blank=True, to='consulta.Disciplina', null=True),
        ),
    ]
