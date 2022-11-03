from django.shortcuts import render
from .models import Produtos

# Create your views here.

def index(request):
    produtos = Produtos.objects.all
    return render(request, 'lojaSite/index.html',{'produtos' : produtos})