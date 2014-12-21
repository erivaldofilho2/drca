# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditos',
            old_name='n_cred',
            new_name='disc_cred',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='nome_departamento',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='credtos',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='scretaria',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='n_credito',
        ),
        migrations.AddField(
            model_name='aluno',
            name='credito',
            field=models.ForeignKey(to='consulta.Creditos', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='consulta.Curso', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso',
            name='secretaria',
            field=models.ForeignKey(to='consulta.Secretaria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='credito',
            field=models.ForeignKey(to='consulta.Creditos', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to=b'consulta.Disciplina', null=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(to='consulta.Curso', null=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(to='consulta.Professor', null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='departamento',
            field=models.ForeignKey(to='consulta.Departamento', null=True),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='departamento',
            field=models.ForeignKey(to='consulta.Departamento', null=True),
        ),
    ]
