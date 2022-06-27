from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.session.get('usuario'):
        return HttpResponse('Olá')
    else:
        return redirect('/auth/login/?status=2')
