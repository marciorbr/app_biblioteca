from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('descricao_livro/<int:id>', views.descricao_livro, name='descricao_livro'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar_emprestimo/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),
]