from django.db import models

# Create your models here.
class Creditos(models.Model):
    
    disc_cred = models.IntegerField()
    cred_obrigatorios = models.IntegerField()
    cred_eletivos = models.IntegerField()
    
    def __str__(self):
        return unicode(self.disc_cred)

class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, null=True)
    
    def __str__(self):
        return self.nome
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=30)
    tipo = models.IntegerField()  
    departamento = models.ForeignKey(Departamento, null=True)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome =  models.CharField(max_length=30)
    secretaria = models.ForeignKey(Secretaria, null=True)
    
    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=10)
    disciplina_requisito = models.ForeignKey( 'self', null=True, blank=True)
    credito = models.ForeignKey(Creditos, null=True)
    status = models.CharField(max_length=30)
    eletiva_obrigatoria = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, null=True)
    professor = models.ForeignKey(Professor, null=True)
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, null=True)
    matricula = models.IntegerField()
    credito = models.ForeignKey(Creditos, null=True)
    disciplinas = models.ManyToManyField(Disciplina, null=True, blank=True)
    
    def verifica_pre_requisito(self,id):
        status = 0
        for disc in self.disciplinas.all():
            print disc
            print disc.id,"==",id
            if disc.id == id:
                status = 1
                break
            else:
                status = 0
        return status
        
    def __str__(self):
        return self.nome

    
