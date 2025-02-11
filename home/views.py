from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def local(request):
    return render(request, 'local.html')

def exibiritem(request, id):
    return render(request, 'exibiritem.html', {'id': id})

def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario': usuario})

def dia_da_semana(request, num):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    dia = dias.get(num, "Número inválido! Escolha um número entre 1 e 7.")
    return render(request, 'dia.html', {'dia': dia})

def form(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        data_nascimento = request.POST.get('data_nascimento')
        rg = request.POST.get('rg')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        # Armazenar os dados na sessão
        request.session['dados_cliente'] = {
            'nome_completo': nome_completo,
            'data_nascimento': data_nascimento,
            'rg': rg,
            'cpf': cpf,
            'telefone': telefone,
            'email': email,
            'endereco': endereco
        }

        # Redirecionar para a view 'dados'
        return redirect(reverse('dados'))

    return render(request, 'form.html')

def dados(request):
    dados_cliente = request.session.get('dados_cliente', {})
    return render(request, 'dados.html', dados_cliente)

LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Maria Oliveira", "matricula": "202302", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Carlos Souza", "matricula": "202303", "curso": "Técnico em Informática", "turma": "208"},
]

def listar_alunos(request):
    context = {
        'lista': [(indice, aluno) for indice, aluno in enumerate(LISTA_ALUNOS)],
    }
    return render(request, 'listar_alunos.html', context)

def editar_aluno(request, indice):
    aluno = LISTA_ALUNOS[indice]

    if request.method == "POST":
        aluno['nome'] = request.POST.get("nome")
        aluno['matricula'] = request.POST.get("matricula")
        aluno['curso'] = request.POST.get("curso")
        aluno['turma'] = request.POST.get("turma")

        return redirect('listar_alunos')

    context = {
        'aluno': aluno,
        'indice': indice
    }
    return render(request, 'form_aluno.html', context)

def cadastrar_aluno(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        matricula = request.POST.get("matricula")
        curso = request.POST.get("curso")
        turma = request.POST.get("turma")

        novo_aluno = {
            "nome": nome,
            "matricula": matricula,
            "curso": curso,
            "turma": turma
        }
        LISTA_ALUNOS.append(novo_aluno)
        return redirect('listar_alunos')
    
    return render(request, 'form_aluno.html', {}) 

def excluir_aluno(request, indice):
    del LISTA_ALUNOS[indice]
    return redirect('listar_alunos')