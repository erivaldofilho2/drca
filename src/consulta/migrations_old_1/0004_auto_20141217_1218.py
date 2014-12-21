# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_disciplina_disciplina_pre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='credtos',
            new_name='credito',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='nome_text',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='creditos',
            old_name='disc_n_cred',
            new_name='disc_cred',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='scretaria',
            new_name='secretaria',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='nome_departamento',
            new_name='nome',
        ),
    ]
