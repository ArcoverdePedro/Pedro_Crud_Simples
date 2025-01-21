from django.shortcuts import render
from .models import Pessoa
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PessoaForm


# Create your views here.
def home(request):
    """Página que lista todos os produtos, com possibilidade de ordenação"""
    pessoas = Pessoa.objects.all().order_by('nome') # Ordenado pelo nome das pessoas (a ao z)
    return render(request, 'home.html', {'pessoas': pessoas})


def add_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova pessoa
            return redirect('home')  # Redireciona para o home
    else:    
        form = PessoaForm()
    return render(request, 'add_pessoa.html', {'form': form})

def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('home')  # Redireciona para o home
    else:    
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})

def deletar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()  # Deleta a pessoa cadastrada
        return redirect('home')  # Redireciona para o home
    return render(request, 'deletar_pessoa.html', {'pessoa': pessoa})