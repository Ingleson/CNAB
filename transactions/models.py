from django.db import models
from django.utils import timezone

class TypeTransaction(models.TextChoices):
    DEFAULT = None
    DEBITO = 1
    BOLETO = 2
    FINANCIAMENTO = 3
    CREDITO = 4
    EMPRESTIMO = 5
    VENDAS = 6
    TED = 7
    DOC = 8
    ALUGUEL = 9

class Transaction(models.Model):
    class Meta:
        ordering = ['id']

    typetransaction = models.CharField(
        choices=TypeTransaction.choices,
        default=TypeTransaction.DEFAULT,
        max_length=20
    )
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name='transactions'
    )