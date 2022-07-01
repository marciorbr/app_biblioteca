from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('descricao_livro/<int:id>', views.descricao_livro, name = 'descricao_livro'),
]