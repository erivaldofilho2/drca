# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('matricula', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Creditos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disc_cred', models.IntegerField()),
                ('cred_obrigatorios', models.IntegerField()),
                ('cred_eletivos', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=30)),
                ('eletiva_obrigatoria', models.CharField(max_length=30)),
                ('credito', models.ForeignKey(to='consulta.Creditos', null=True)),
                ('curso', models.ForeignKey(to='consulta.Curso', null=True)),
                ('disciplina_requisito', models.ForeignKey(blank=True, to='consulta.Disciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('departamento', models.ForeignKey(to='consulta.Departamento', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('tipo', models.IntegerField()),
                ('departamento', models.ForeignKey(to='consulta.Departamento', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(to='consulta.Professor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso',
            name='secretaria',
            field=models.ForeignKey(to='consulta.Secretaria', null=True),
            preserve_default=True,
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
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to='consulta.Disciplina', null=True, blank=True),
            preserve_default=True,
        ),
    ]
