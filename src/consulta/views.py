from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.context_processors import request
from django.http.response import HttpResponse
from consulta.models import *
from django.template import Context, loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    contexto = Context({'teste':'Erivaldo'})
    return HttpResponse(template.render(contexto))

def disciplinas(request):
    disciplinas = Disciplina.objects.all()
    template = loader.get_template('disciplinas.html')
    contexto = Context({'disciplinas':disciplinas,})
    return HttpResponse(template.render(contexto))

def info_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id = disciplina_id)    
    lista = disciplina.aluno_set.all()       
    cred = disciplina.credito.disc_cred
    cred_min = disciplina.credito.cred_obrigatorios 
    template = loader.get_template("info_disciplina.html")
    contexto = Context({'disciplina':disciplina,'alunos':lista,'cred':cred,'cred_min': cred_min})
    return HttpResponse(template.render(contexto))

def aluno(request):
    alunos = Aluno.objects.all()
    template = loader.get_template('alunos.html')
    contexto = Context({'alunos':alunos})
    return HttpResponse(template.render(contexto))

def info_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id = aluno_id)    
    disciplinas = aluno.disciplinas.all()  
    template = loader.get_template("info_aluno.html")
    contexto = Context({'aluno':aluno,'disciplinas':disciplinas,'teste':'teste'})
    return HttpResponse(template.render(contexto))


def departamento(request):
    disciplinas = Disciplina.objects.all()
    departamentos = Departamento.objects.all()
    secretarias = Secretaria.objects.all()
    template = loader.get_template('departamento.html')
    contexto = Context({'disciplinas':disciplinas, 'departamentos':departamentos,'secretarias':secretarias})
    return HttpResponse(template.render(contexto))

def matricula(request):
    alunos = Aluno.objects.all()
    template = loader.get_template('matricula.html')
    contexto = Context({'alunos':alunos,})
    return HttpResponse(template.render(contexto))

def matricular_aluno(request,aluno_id):
    aluno = Aluno.objects.get(id = aluno_id )
    curso_aluno = aluno.curso.id
    pos_graduacao = []
    lista = []
    for disc in Disciplina.objects.all():
        if disc.curso.secretaria.tipo is 2:
            if disc.curso.secretaria.departamento.id == aluno.curso.secretaria.departamento.id:
                pos_graduacao.append(disc)
    for disc in Disciplina.objects.filter(curso=curso_aluno):
        if disc.curso.secretaria.tipo is 1:
            lista.append(disc)
    template = loader.get_template('matricular_aluno.html')
    contexto = Context({'disciplinas':lista,'aluno':aluno,'pos_graduacao':pos_graduacao})
    return HttpResponse(template.render(contexto))

def matricular_diciplina(request,disciplina_id,aluno_id):
    aluno = Aluno.objects.get(id = aluno_id )
    disciplina = Disciplina.objects.get(id = disciplina_id)
    status = 300
    if(aluno.curso.secretaria.tipo is 1 and disciplina.curso.secretaria.tipo is 2):
        if(aluno.credito.cred_obrigatorios < 170):
            status = 3
        else:
            aluno.disciplinas.add(disciplina)
            status = 1
    else:
        if(disciplina.credito.cred_obrigatorios <= aluno.credito.cred_obrigatorios):
            if(len(aluno.disciplinas.all()) is not 0):
                if(disciplina.disciplina_requisito is not None and aluno.verifica_pre_requisito(disciplina.disciplina_requisito.id)):
                    aluno.disciplinas.add(disciplina)
                    status = 1
                elif disciplina.disciplina_requisito is None:
                    aluno.disciplinas.add(disciplina)
                    status = 1
                else:
                    status = 2
            elif len(aluno.disciplinas.all()) is 0 and disciplina.disciplina_requisito is None:
                aluno.disciplinas.add(disciplina)
                status = 1
            else:
                status = 2
            
        else:
            status = 0
    template = loader.get_template('verifica_matricula.html')
    contexto = Context({'status':status,'aluno':aluno,'disciplina':disciplina})
    return HttpResponse(template.render(contexto)) 