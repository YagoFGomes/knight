from django.shortcuts import render, redirect
from apps.painel.models import Email
from django.contrib import messages

# Create your views here.

def Pagina_Inicial(request):
    if request.POST: 
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Email.objects.create(name=name, email=email, subject=subject, message=message)
        messages.add_message(request, messages.SUCCESS, 'Seu e-mail enviado com sucesso!')

    return render(request, 'index.html')
