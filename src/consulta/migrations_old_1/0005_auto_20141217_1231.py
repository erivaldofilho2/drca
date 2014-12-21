# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0004_auto_20141217_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='disciplina_pre',
            field=models.ManyToManyField(related_name='disciplina_pre_rel_+', null=True, to=b'consulta.Disciplina', blank=True),
        ),
    ]
