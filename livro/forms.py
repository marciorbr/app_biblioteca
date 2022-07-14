from django import forms
from django.db.models import fields
from .models import Livros, Categoria, Emprestimos

class CadastroLivro(forms.ModelForm):
    
    class Meta:
        model = Livros
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class CadastroCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class CadastroEmprestimo(forms.ModelForm):

    class Meta:
        model = Emprestimos
        fields = "__all__"