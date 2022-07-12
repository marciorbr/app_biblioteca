from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from livro.models import Emprestimos, Livros, Categoria
from .forms import CadastroLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter( usuario = usuario )
        usuario_logado = request.session.get('usuario')
        return render(request,'home.html', {'livros': livros, 'usuario_logado': usuario_logado})
    else:
        return redirect('/auth/login/?status=2')
    
def descricao_livro(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            usuario_logado = request.session.get('usuario')
            return render(request, 'descricao_livro.html', {'livro': livros, 
                                                            'categoria_livro': categoria_livro,
                                                            'emprestimos': emprestimos, 
                                                            'usuario_logado': usuario_logado })
        else:
            return HttpResponse('Este livro não é seu')
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        if form.is_valid():
            form.save()
            usuario_logado = request.session.get('usuario')
            form = CadastroLivro()
            return render(request, 'cadastrar_livro.html', {'usuario_logado': usuario_logado,
                                                            'formCadastroLivro': form})
        else:
            return HttpResponse('Dados inválidos!')

    if request.session.get('usuario'):
        usuario_logado = request.session.get('usuario')
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario_logado)
        return render(request, 'cadastrar_livro.html', {'usuario_logado': usuario_logado, 
                                                        'formCadastroLivro': form})
    else:
        return redirect('/auth/login/?status=2')
