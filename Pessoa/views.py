from multiprocessing import context
from django.shortcuts import render
from .models import PessoaModel
# Create your views here.

def listar(request):
    return render(request,'lista_pessoa.html')
