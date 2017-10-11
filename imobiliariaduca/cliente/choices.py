from djchoices import DjangoChoices, C

class ContaStatus(DjangoChoices):
    Ativo = C(value='Ativo', label='Ativo')
    Atrasado = C(value='Atrasado', label='PagamentoAtrasado')
    SuspensoPgto = C(value='SuspensoPgto', label='SuspensaFaltaPGTO')
    Inativo = C(value='Inativo', label='Inativo')
    Banido = C(value='Banido', label='Banido')


class ContaTipo(DjangoChoices):
    Pi = C(value='PI', label='Pessoa'),
    PF = C(value='PF', label='Pessoa Fisica'),
    PJ = C(value='PJ', label='Pessoa Juridica')
