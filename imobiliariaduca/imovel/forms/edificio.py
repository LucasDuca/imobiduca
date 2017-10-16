# coding: utf-8
from django.contrib.auth.models import User
from django import forms
from suit.widgets import NumberInput, HTML5Input, TextInput

from cliente.models.conta import Conta
from imovel.models.edificio import Edificio
from django.core.exceptions import ValidationError
from base.utils import validate_cnpj, validate_cpf
from imovel.choices import ESTADOS, StatusVenda, TipoImovel


class EdificioForm(forms.ModelForm):

    fields = ['nome', 'image', 'tipo', 'status', 'valor', 'usuario',
              'cep',
              'logradouro', 'numero', 'complemento',
              'bairro', 'cidade',
              'estado',]
    #fields = ('cpfcnpj', 'cliente_tipo')
    nome = forms.CharField(required=True)
    image = forms.ImageField(required=True, label='Foto')
    tipo = forms.ChoiceField(required=True,choices=TipoImovel.choices)
    status = forms.ChoiceField(required=True, choices=StatusVenda.choices)
    valor = forms.CharField(required=True)



    usuario = forms.widgets.Select(attrs={'readonly': True, 'disabled': 'True'})

    logradouro = forms.CharField(required=False,max_length=255, label='Logradouro')
    numero = forms.IntegerField(required=False,label=u'Número', initial=0)
    complemento = forms.CharField(required=False, max_length=100, label='Complemento')
    bairro = forms.CharField(required=False,max_length=30, label='Bairro')
    cidade = forms.CharField(required=False,max_length=30, initial="Rio de Janeiro", label='Cidade')
    cep = forms.CharField(required=False,max_length=9, label='CEP')
    estado = forms.CharField(max_length=2, required=False, initial='RJ')


    def clean(self):
        cleaned_data = super(EdificioForm, self).clean()
        return cleaned_data

    class Meta:
        model = Edificio
        fields = ['nome', 'image', 'tipo', 'status', 'valor', 'usuario','dono',
                  'cep',
                  'logradouro', 'numero', 'complemento',
                  'bairro', 'cidade',
                  'estado', ]

        widgets = {'usuario': forms.widgets.Select(attrs={'readonly': True,
                                                      'disabled': True}),
                   'dono': forms.widgets.Select(attrs={'readonly': True,
                                                          'disabled': True})
                   }

    def save(self, commit=True):
        e = super(EdificioForm, self).save(commit=False)
        # do custom stuff
        if commit:
            e.save()
        return e



