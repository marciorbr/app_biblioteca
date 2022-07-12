from django import forms
from django.db.models import fields
from .models import Livros

class CadatroLivro(forms.ModelForm):

    class Meta:
        model = Livros
        fields = "__all__"

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['usuario'].widget = forms.HiddenInput()