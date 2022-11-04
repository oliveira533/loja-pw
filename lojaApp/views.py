from django.shortcuts import render
from .models import Produtos

# Create your views here.

def index(request):
    produtos = Produtos.objects.all
    return render(request, 'lojaSite/index.html',{'produtos' : produtos})

def produtodesc(request, produto_id):
    produto = Produtos.objects.get(id=produto_id)
    return render(request, 'lojaSite/produtodesc.html', {'produto':produto})