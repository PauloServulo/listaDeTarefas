from django.db import models

# Create your models here.
# model que representa uma tarefa
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Tarefas'
    
    def __str__(self):
        return self.nome
