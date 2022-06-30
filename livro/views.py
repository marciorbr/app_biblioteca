from django.shortcuts import render, redirect
from usuarios.models import Usuario
from livro.models import Livros

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter( usuario = usuario )
        return render(request,'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')
