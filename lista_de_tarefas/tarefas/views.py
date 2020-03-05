from django.shortcuts import render, redirect
from .models import Tarefa
from .form import TarefaForm
# Create your views here.

#Página inicial
def index(request):
    dados = {}
    dados['tarefas'] = Tarefa.objects.all()
    return render(request, 'tarefas/index.html', dados)

#Inserir uma nova tarefa na lista
def insere_tarefa(request):
    form = TarefaForm(request.POST or None)
    dados = {}
    dados['form'] = form
    dados['tipo'] = 1
    if form.is_valid():
        form.save()
        return redirect('url_index')
    return render(request, 'tarefas/insere.html', dados)

#Atualiza uma tarefa de acordo com o id informado
def edita_tarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    dados = {}
    dados['form'] = form
    dados['tipo'] = 2
    if form.is_valid():
        form.save()
        return redirect('url_index')
    return render(request, 'tarefas/insere.html', dados)

#Deleta uma tarefa de acordo com o id informado
def deleta_tarefa(request,pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.delete()
    return redirect('url_index')
