from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Tarefa
from .form import TarefaForm
from django.urls import reverse_lazy

class TasksListView(ListView):
    model = Tarefa
    template_name = 'tarefas/index.html'
    context_object_name = 'tarefas'

class TasksEditView(UpdateView):
    model = Tarefa
    template_name = 'tarefas/insere.html'
    form_class = TarefaForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super(TasksEditView, self).get_context_data(**kwargs)
        context['tipo'] = 2
        return  context

class TasksCreateView(CreateView):
    model = Tarefa
    template_name = 'tarefas/insere.html'
    form_class = TarefaForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super(TasksCreateView, self).get_context_data(**kwargs)
        context['tipo'] = 1
        return context

class TasksDeleteView(DeleteView):
    model = Tarefa
    success_url = '/'

# #Inserir uma nova tarefa na lista
# def insere_tarefa(request):
#     form = TarefaForm(request.POST or None)
#     dados = {}
#     dados['form'] = form
#     dados['tipo'] = 1
#     if form.is_valid():
#         form.save()
#         return redirect('tarefas:url_index')
#     return render(request, 'tarefas/insere.html', dados)
#
# #Atualiza uma tarefa de acordo com o id informado
# def edita_tarefa(request, pk):
#     tarefa = Tarefa.objects.get(pk=pk)
#     form = TarefaForm(request.POST or None, instance=tarefa)
#     dados = {}
#     dados['form'] = form
#     dados['tipo'] = 2
#     if form.is_valid():
#         form.save()
#         return redirect('tarefas:url_index')
#     return render(request, 'tarefas/insere.html', dados)
#
# #Deleta uma tarefa de acordo com o id informado
# def deleta_tarefa(request,pk):
#     tarefa = Tarefa.objects.get(pk=pk)
#     tarefa.delete()
#     return redirect('tarefas:url_index')
