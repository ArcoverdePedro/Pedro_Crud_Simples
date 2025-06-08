from multiprocessing import context
from venv import create
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
            id_pessoa = request.POST.get('id_pessoa')
            pessoa = get_object_or_404(Pessoa, id=id_pessoa)
            pessoa.delete()
            return redirect('home')
        if 'editar' in request.POST:
            id_pessoa = request.POST.get('id_pessoa')
            pessoa = get_object_or_404(Pessoa, id=id_pessoa)
            pessoa.nome = request.POST.get('nome')
            pessoa.idade = int(request.POST.get('idade'))
            pessoa.cpf = request.POST.get('cpf')
            pessoa.save()
            return redirect('home')
        if 'add_pessoa' in request.POST:
            pessoa = Pessoa.objects.create(
                nome = request.POST.get('nome'),
                idade = int(request.POST.get('idade')),
                cpf = request.POST.get('cpf')
            )
            return redirect('home')
    return render(request, "1_app_aerotur/home/home.html", context)