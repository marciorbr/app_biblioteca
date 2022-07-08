from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from livro.models import Emprestimos, Livros, Categoria

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter( usuario = usuario )
        return render(request,'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')
    
def descricao_livro(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            return render(request, 'descricao_livro.html', {'livro': livros, 'categoria_livro': categoria_livro,
                                                            'emprestimos': emprestimos })
        else:
            return HttpResponse('Este livro não é seu')
    return redirect('/auth/login/?status=2')
