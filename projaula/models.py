from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    presenca = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    nota = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
objetos = models.Manager()
