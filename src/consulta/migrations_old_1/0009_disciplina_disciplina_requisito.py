# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0008_remove_disciplina_disciplina_requisito'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_requisito',
            field=models.ForeignKey(blank=True, to='consulta.Disciplina', null=True),
            preserve_default=True,
        ),
    ]
