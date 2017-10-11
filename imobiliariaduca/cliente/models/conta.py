from django.db import models
from cliente.choices import ContaStatus, ContaTipo
from datetime import date, datetime


class Conta(models.Model):
    nome = models.CharField(max_length=55, blank=False, null=False)
    cpfcnpj = models.CharField(max_length=14)
    status = models.CharField(max_length=20, choices=ContaStatus.choices, default=ContaStatus.Ativo)

    data_nascimento = models.DateField(
        null=True, blank=True, default=None,
        verbose_name="Data de Nascimento", help_text="Data de Nascimento de um cliente."
    )

    data_cadastro = models.DateTimeField(
        verbose_name="Data de cadastro", auto_now_add=True,
        help_text="Data em que o cadastro do cliente foi efetuado."
    )

    data_atualizacao = models.DateTimeField('Atualizado em', auto_now=True)

    cliente_tipo = models.CharField(
        max_length=3, choices=ContaTipo.choices, default='PF',
        verbose_name="Tipo de Cliente",
        help_text="Pessoa Fisica ou Pessoa Juridica."
    )

    fim = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s - %s " % (self.nome, self.status)

    def Meta(self):
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'