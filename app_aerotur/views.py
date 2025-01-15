from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProdutoForm


# Create your views here.
def home(request):
    """Página que lista todos os produtos, com possibilidade de ordenação"""
    # Recupera o parâmetro ordem da URL
    ordem = request.GET.get('ordem', 'nome')  # ordem padrão por nome

    if ordem == 'preco':
        produtos = Produto.objects.all().order_by('preco')  # Ordena por preço (menor ao maior)
    else:
        produtos = Produto.objects.all().order_by('nome')  # Ordena por nome (a ao z)
    
    return render(request, 'home.html', {'produtos': produtos, 'ordem': ordem})


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo produto
            return redirect('home')  # Redireciona para o home
    else:    
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('home')  # Redireciona para o home
    else:    
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()  # Deleta o produto
        return redirect('home')  # Redireciona para o home
    return render(request, 'deletar_produto.html', {'produto': produto})