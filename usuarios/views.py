from django.shortcuts import render, redirect
from django.http import HttpResponse
from hashlib import sha256
from .models import Usuario

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', { 'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')
    
    usuario = Usuario.objects.filter(email = email)
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadatro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          senha = senha,
                          email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    
    except:
        return redirect('/auth/cadastro/?status=4')
    
def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    return HttpResponse(f"{email} {senha}")