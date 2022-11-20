from django.shortcuts import render

# Create your views here.
def Painel_Administracao(request):
    return render(request, 'painel_admin.html')