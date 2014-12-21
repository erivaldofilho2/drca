# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_disciplina_disciplina_requisito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to=b'consulta.Disciplina', null=True, blank=True),
        ),
    ]
