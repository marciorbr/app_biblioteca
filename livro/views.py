from django.shortcuts import render, redirect
from usuarios.models import Usuario

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        return render(request,'home.html')
    else:
        return redirect('/auth/login/?status=2')
