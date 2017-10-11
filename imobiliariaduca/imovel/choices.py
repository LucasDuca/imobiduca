# coding: utf-8
from djchoices import DjangoChoices, C

from localflavor.br import br_states

ESTADOS = STATE_CHOICES = (
    ('RJ', 'Rio de Janeiro'),
) + br_states.STATE_CHOICES

class TipoImovel(DjangoChoices):
    Casa = C(value='Casa', label='Casa')
    Apartamento = C(value='Apartamento', label='Apartamento')
    Loja = C(value='Loja', label='Loja')

class StatusVenda(DjangoChoices):
    Vendido = C(value='Cancelado', label='Cancelado')
    Alugado = C(value='Alugado', label='Alugado')
    Aguardando = C(value='Aguardando', label='Aguardando por Locador')

