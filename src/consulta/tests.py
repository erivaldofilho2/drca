from django.test import TestCase
from django.test import Client
from consulta.models import *
from twisted.spread.pb import respond

# Create your tests here.
class Teste_geral(TestCase):

       def test_verifica_pre_requisito(self):
           aluno = Aluno.objects.get(id=6)
           self.assertEqual(0, aluno.verifica_pre_requisito(1))
           aluno.disciplinas.append(Disciplina.objects.get(id=2))
           self.assertEqual(1,aluno.verifica_pre_requisito(1))
        
       def test_matricula_response(self):
           c = Client()
           response = c.get('/matricula/6/matricular_aluno/1')
           status = response.context['status']
           self.assertEqual(2,status)#não satifaz o pré-requisito
           response = c.get('/matricula/3/matricular_aluno/6')
           status = response.context['status']
           self.assertEqual(0,status)#não possui credito suficiente
           response = c.get('/matricula/3/matricular_aluno/5')
           status = response.context['status']
           self.assertEqual(1,status)#matriculado com sucesso
           response = c.get('/matricula/6/matricular_aluno/8')
           status = response.context['status']
           self.assertEqual(3,status)#matricular em materia de pos-graduação
            
       def test_info_aluno(self):
           c = Client()
           response = c.get('/aluno/6/info_aluno/')
           aluno = response.context['aluno']
           self.assertEqual('Erivaldo Lourenco',aluno.nome)
           self.assertEqual(6,aluno.id)
           self.assertEqual(1,aluno.curso.id)
         
       def test_pagina_info_aluno(self):
           c = Client()   
           aluno = Aluno.objects.get(id = 2)    
           disciplinas = aluno.disciplinas.all()
           response = c.post('/aluno/2/info_aluno/', {'aluno':aluno,'disciplinas':disciplinas})
           self.assertEqual(200,response.status_code)
       
       def test_info_disciplina(self):
           c = Client()
           response = c.get('/disciplinas/3/info_disciplina/')
           disciplina = response.context['disciplina']
           self.assertEqual('Projeto de Sistema de Software', disciplina.nome)
           self.assertEqual(3, disciplina.id)
           self.assertEqual('INF 1624', disciplina.codigo)
       
    
       def test_paginas_disciplina(self):
           c = Client()
           disciplinas = Disciplina.objects.all()
           response = c.post('/disciplinas/',{'disciplinas':disciplinas})
           self.assertEqual(200,response.status_code)
           disc = Disciplina.objects.get(id = 2)    
           lista = disc.aluno_set.all()       
           cred = disc.credito.disc_n_cred
           cred_min = disc.credito.cred_eletivos    
           response = c.post('/disciplinas/2/info_disciplina/',{'disciplina':disc,'alunos':lista,'cred':cred,'cred_min': cred_min})
           self.assertEqual(200,response.status_code)
        