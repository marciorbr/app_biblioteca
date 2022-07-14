from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length = 100, null=True)
    autor = models.CharField(max_length= 30, null=True)
    co_autor = models.CharField(max_length= 30, blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank= True, null= True)
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank= True, null= True)
    data_emprestimo = models.DateField(default=date.today)
    data_devolucao = models.DateTimeField(blank= True, null= True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        if self.nome_emprestado_anonimo == None:
            return f"{self.nome_emprestado} | {self.livro}"
        else:
            return f"{self.nome_emprestado_anonimo} | {self.livro}"