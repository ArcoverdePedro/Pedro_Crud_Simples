from django import forms
from .models import Produto, Pessoa

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'quantidade_estoque']  # Não inclui 'data_criacao

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','idade','cpf']
