from django.db import models
from datetime import date

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Livros(models.Model):
    nome = models.CharField(max_length = 100, null=True)
    autor = models.CharField(max_length= 30, null=True)
    co_autor = models.CharField(max_length= 30, blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length= 30, blank=True, null=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.nome