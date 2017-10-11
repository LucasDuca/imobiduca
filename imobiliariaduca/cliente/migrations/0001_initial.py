# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=55)),
                ('cpfcnpj', models.CharField(max_length=14)),
                ('status', models.CharField(default=b'Ativo', max_length=20, choices=[(b'Ativo', b'Ativo'), (b'Atrasado', b'PagamentoAtrasado'), (b'SuspensoPgto', b'SuspensaFaltaPGTO'), (b'Inativo', b'Inativo'), (b'Banido', b'Banido')])),
                ('data_nascimento', models.DateField(default=None, help_text=b'Data de Nascimento de um cliente.', null=True, verbose_name=b'Data de Nascimento', blank=True)),
                ('data_cadastro', models.DateTimeField(help_text=b'Data em que o cadastro do cliente foi efetuado.', verbose_name=b'Data de cadastro', auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name=b'Atualizado em')),
                ('cliente_tipo', models.CharField(default=b'PF', help_text=b'Pessoa Fisica ou Pessoa Juridica.', max_length=3, verbose_name=b'Tipo de Cliente', choices=[(b'PJ', b'Pessoa Juridica')])),
                ('fim', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
