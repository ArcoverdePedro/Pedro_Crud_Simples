from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)]  # Validador para garantir que o preço seja maior que zero
    )
    quantidade_estoque = models.IntegerField(
        validators=[MinValueValidator(0)]  # Validador para garantir que a quantidade em estoque seja maior ou igual a zero
    )
    data_criacao = models.DateTimeField(auto_now_add=True)  # Gerado automaticamente

    def __str__(self):
        return self.nome