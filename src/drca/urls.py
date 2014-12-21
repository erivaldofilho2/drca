from django.conf.urls import patterns, include, url
from django.contrib import admin
from consulta import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', views.index, name='index'),
    
    
    
    url(r'^aluno/$', views.aluno, name='aluno'),
    url(r'^aluno/(?P<aluno_id>\d+)/info_aluno/$', views.info_aluno, name='info_aluno'),
    
    url(r'^departamento/$', views.departamento, name='departamento'),
    
    url(r'^disciplinas/$', views.disciplinas, name='disciplinas'),
    url(r'^disciplinas/(?P<disciplina_id>\d+)/info_disciplina/$', views.info_disciplina, name='info_disciplina'),
	url(r'^departamento/(?P<disciplina_id>\d+)/info_disciplina/$', views.info_disciplina, name='info_disciplina'),
    
    url(r'^matricula/(?P<aluno_id>\d+)/matricular_aluno/(?P<disciplina_id>\d+)$', views.matricular_diciplina, name='matricular_diciplina'),
    
    
    url(r'^matricula/$', views.matricula, name='matricula'),
    url(r'^matricula/(?P<aluno_id>\d+)/matricular_aluno/$', views.matricular_aluno, name='matricular_aluno'),


)
