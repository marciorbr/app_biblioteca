from django import forms
from django.db.models import fields
from .models import Livros

class CadatroLivro(forms.ModelForm):

    class Meta:
        model = Livros
        fields = ['nome', 'autor', 'co_autor', 'data_cadastro', 'emprestado','categoria']