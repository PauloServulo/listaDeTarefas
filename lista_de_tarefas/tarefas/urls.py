from django.urls import path

from lista_de_tarefas.tarefas.views import TasksListView, TasksEditView, TasksCreateView, TasksDeleteView
app_name = "tarefas"

urlpatterns = [
    path('', TasksListView.as_view(), name='url_index'),
    path('edit/<int:pk>', TasksEditView.as_view(), name='url_edita'),
    path('insert', TasksCreateView.as_view(), name='url_insere'),
    path('delete/<int:pk>', TasksDeleteView.as_view(), name='url_deleta'),
]