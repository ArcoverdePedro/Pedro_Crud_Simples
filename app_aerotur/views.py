from multiprocessing import context
from venv import create
from django.shortcuts import render
from .models import Pessoa
from django.shortcuts import render, get_object_or_404, redirect



# Create your views here.
def home(request):
    context = {}
    """Página que lista todos os produtos, com possibilidade de ordenação"""
    pessoas = Pessoa.objects.all().order_by('nome')
    context['pessoas'] = pessoas
    if request.method == 'POST':
        if 'deletar' in request.POST:
            id_pessoa = request.get.POST['deletar']
            pessoa = get_object_or_404(Pessoa, id=id_pessoa)
            pessoa.delete()
            return redirect('home')
        if 'editar' in request.POST:
            id_pessoa = request.get.POST['editar']
            pessoa = get_object_or_404(Pessoa, id=id_pessoa)
            pessoa.nome = request.get.POST['nome']
            pessoa.idade = request.get.POST['idade']
            pessoa.cpf = request.get.POST['cpf']
            pessoa.save()
            return redirect('home')
        if 'add_pessoa' in request.POST:
            pessoa = Pessoa.objects.create(
                nome = request.get.POST['nome'],
                idade = request.get.POST['idade'],
                cpf = request.get.POST['cpf']
            )
            return redirect('home')
    return render(request, 'home.html', context)