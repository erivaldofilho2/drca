# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0002_auto_20141217_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_requisito',
            field=models.ForeignKey(blank=True, to='consulta.Disciplina', null=True),
            preserve_default=True,
        ),
    ]
