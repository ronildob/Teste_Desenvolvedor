
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

def home(request):
    return render(request, "home.html", {'titulo': 'Página Principal'})

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        # Validações básicas
        if not nome or not email or not senha:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return redirect('cadastrar')
        
        if len(senha) < 6:
            messages.error(request, 'A senha deve ter pelo menos 6 caracteres.')
            return redirect('cadastrar')

        # Verificar se o e-mail já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('cadastrar')

        # Criar usuário
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('lista_completa')

    return render(request, 'cadastrar.html', {'titulo': 'Página de Cadastro'})

def lista_completa(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar.html', {'usuarios': usuarios, 'titulo': 'Lista de Usuários'})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.nome = request.POST['nome']
        usuario.email = request.POST['email']
        usuario.senha = request.POST['senha']
        usuario.save()
        messages.success(request, "Usuário atualizado com sucesso!")
        return redirect('lista_completa')
    
    return render(request, 'editar.html', {'usuario': usuario, 'titulo': 'Edição de Usuário'})

def excluir(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request, "Usuário excluído com sucesso!")
    return redirect('lista_completa')


