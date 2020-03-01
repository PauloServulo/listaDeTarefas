from django.forms import ModelForm
from .models import Tarefa

#Auxilia na criação dos formulários
class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'data', 'hora', 'descricao']