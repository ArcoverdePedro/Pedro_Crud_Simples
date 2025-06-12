from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .utils import validador


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(
        validators=[MinValueValidator(18)]  # Validador de idade minima de 18 anos
    )
    cpf = models.CharField(max_length=11)

    def clean(self):
        if not validador(self.cpf):
            raise ValidationError("CPF inválido")

    def __str__(self):
        return self.nome
