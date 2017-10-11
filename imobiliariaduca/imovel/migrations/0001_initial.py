# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to=b'imovel/images', verbose_name=b'Imagens')),
                ('valor', models.DecimalField(max_digits=9, decimal_places=2)),
                ('tipo', models.CharField(help_text=b'Tipo de Im\xc3\xb3vel.', max_length=20, verbose_name=b'Tipo de Im\xc3\xb3vel', choices=[(b'Casa', b'Casa'), (b'Apartamento', b'Apartamento'), (b'Loja', b'Loja')])),
                ('status', models.CharField(default=b'Aguardando', help_text=b'Status da Venda do Im\xc3\xb3vel.', max_length=20, verbose_name=b'Status da Venda', choices=[(b'Cancelado', b'Cancelado'), (b'Alugado', b'Alugado'), (b'Aguardando', b'Aguardando por Locador')])),
                ('data_cadastro', models.DateTimeField(help_text=b'Data em que foi cadastrado o im\xc3\xb3vel.', verbose_name=b'Data de cadastro', auto_now_add=True)),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.PositiveIntegerField()),
                ('complemento', models.CharField(max_length=100, null=True)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(default=b'Rio de Janeiro', max_length=30)),
                ('estado', models.CharField(default=b'RJ', max_length=2, choices=[(b'RJ', b'Rio de Janeiro'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('cep', models.CharField(max_length=9)),
                ('dono', models.OneToOneField(related_name='proprietario', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
