from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Email

from django.contrib import messages


@login_required(login_url='/painel-admin/login/')
def Painel_Administracao(request):
    username = request.user.username
    context={
        'username':username,
    }
    return render(request, 'painel_admin.html', context)

@login_required(login_url='/painel-admin/login/')
def Emails(request):
    username = request.user.username
    emails = Email.objects.all().order_by('-date')
    context={
        'username':username,
        'emails':emails,
    }
    return render(request, 'emails.html', context)

def Login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/painel-admin/')
        else:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('/painel-admin/login/')