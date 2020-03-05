from django.urls import path

#from lista_de_tarefas.tarefas.templates import views
from lista_de_tarefas.tarefas.views import index, insere_tarefa, edita_tarefa, deleta_tarefa
app_name = "tarefas"

urlpatterns = [
    path('', index, name='url_index'),
    path('insere/', insere_tarefa, name='url_insere'),
    path('edita/<int:pk>/', edita_tarefa, name='url_edita'),
    path('deleta/<int:pk>/', deleta_tarefa, name='url_deleta'),
]