from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from livro.models import Emprestimos, Livros, Categoria
from .forms import CadastroLivro, CadastroCategoria, CadastroEmprestimo

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status_categoria = request.GET.get('cadastro_categoria')
        livros = Livros.objects.filter( usuario = usuario )
        formCadastroEmprestimo = CadastroEmprestimo()
        usuario_logado = request.session.get('usuario')
        return render(request,'home.html', {'livros': livros, 
                                            'usuario_logado': usuario_logado,
                                            'status_categoria': status_categoria,
                                            'formCadastroEmprestimo': formCadastroEmprestimo,})
    else:
        return redirect('/auth/login/?status=2')
    
def descricao_livro(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            formCadastroEmprestimo = CadastroEmprestimo()
            usuario_logado = request.session.get('usuario')
            return render(request, 'descricao_livro.html', {'livro': livros, 
                                                            'categoria_livro': categoria_livro,
                                                            'emprestimos': emprestimos, 
                                                            'usuario_logado': usuario_logado,
                                                            'id_livro': id,
                                                            'formCadastroEmprestimo': formCadastroEmprestimo,})
        else:
            return HttpResponse('Este livro não é seu')
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        formCadastroLivro = CadastroLivro(request.POST)
        if formCadastroLivro.is_valid():
            formCadastroLivro.save()
            usuario_logado = request.session.get('usuario')
            formCadastroLivro = CadastroLivro()
            formCadastroEmprestimo = CadastroEmprestimo()
            usuario = Usuario.objects.get(id = request.session['usuario'])
            livros = Livros.objects.filter( usuario = usuario )

            return render(request,'home.html', {'livros': livros, 
                                                'usuario_logado': usuario_logado,
                                                'formCadastroLivro': formCadastroLivro,
                                                'formCadastroEmprestimo': formCadastroEmprestimo,})
        else:
            return HttpResponse('Dados inválidos!')

    if request.session.get('usuario'):
        usuario_logado = request.session.get('usuario')
        formCadastroEmprestimo = CadastroEmprestimo()
        formCadastroLivro = CadastroLivro()
        formCadastroLivro.fields['usuario'].initial = request.session['usuario']
        formCadastroLivro.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario_logado)
        return render(request, 'cadastrar_livro.html', {'usuario_logado': usuario_logado, 
                                                        'formCadastroLivro': formCadastroLivro,
                                                        'formCadastroEmprestimo': formCadastroEmprestimo,})
    else:
        return redirect('/auth/login/?status=2')

def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')

def cadastrar_categoria(request):
    if request.method == 'POST':
        formCadastroCategoria = CadastroCategoria(request.POST)

        if formCadastroCategoria.is_valid():
            formCadastroCategoria.save()
            return redirect('/livro/home?cadastro_categoria=1')
        else:
            return redirect('/livro/home?cadastro_categoria=2')

    elif request.session.get('usuario'):
        usuario_logado = request.session.get('usuario')
        formCadastroCategoria = CadastroCategoria()
        formCadastroEmprestimo = CadastroEmprestimo()
        formCadastroCategoria.fields['usuario'].initial = request.session['usuario']
        return render(request, 'cadastrar_categoria.html', {'usuario_logado': usuario_logado, 
                                                        'formCadastroCategoria': formCadastroCategoria,
                                                        'formCadastroEmprestimo': formCadastroEmprestimo,})
    else:
        return redirect('/auth/login/?status=2')