from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login(request):
    if request.method != 'POST':
        return render(request, 'usuario/login.html')
    email = request.POST.get('InputEmail')
    senha = request.POST.get('InputPassword1')

    if not email or not senha:
        print('Preencha todos os campos')
        messages.add_message(request, messages.ERROR, 'Preencha todos os campos')
        return render(request, 'usuario/login.html')
    
    user = auth.authenticate(request, username=email, password=senha)

    if not user:
        print('Usuário ou senha inválidos')
        messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos')
        return render(request, 'usuario/login.html')
    else:
        print ('Login realizado com sucesso')
        auth.login(request, user)
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'usuario/cadastro.html')
    nome = request.POST.get('InputName')
    email = request.POST.get('InputEmail')
    senha = request.POST.get('InputPassword1')
    senha2 = request.POST.get('InputPassword2')

    if not nome or not email or not senha or not senha2:
        print('Preencha todos os campos')
        messages.add_message(request, messages.ERROR, 'Preencha todos os campos')
        return render(request, 'usuario/cadastro.html')

    try:
        validate_email(email)
    except:
        print('Email inválido')
        messages.add_message(request, messages.ERROR, 'Email inválido')
        return render(request, 'usuario/cadastro.html')

    if senha != senha2:
        print('Senhas não conferem')
        messages. add_message(request, messages.ERROR, 'Senhas não conferem')
        return render(request, 'usuario/cadastro.html')
    
    if len(senha) < 6:
        print('Senha precisa ter no mínimo 6 caracteres')
        messages.add_message(request, messages.ERROR, 'Senha precisa ter no mínimo 6 caracteres')
        return render(request, 'usuario/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        print('Email já cadastrado')
        messages.add_message(request, messages.ERROR, 'Email já cadastrado')
        return render(request, 'usuario/cadastro.html')
    
    if User.objects.filter(username=nome).exists():
        print('Nome já cadastrado')
        messages.add_message(request, messages.ERROR, 'Nome já cadastrado')
        return render(request, 'usuario/cadastro.html')
    
    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'usuario/dashboard.html')

