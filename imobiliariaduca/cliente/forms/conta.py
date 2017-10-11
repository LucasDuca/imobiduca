# coding: utf-8
from django.contrib.auth.models import User
from django import forms
from suit.widgets import NumberInput, HTML5Input, TextInput
from cliente.models.conta import Conta
from django.core.exceptions import ValidationError
from base.utils import validate_cnpj, validate_cpf
from cliente.choices import ContaTipo

class ContaForm(forms.Form):
    model = Conta
    objects = Conta.objects

    fields = ('cpfcnpj', 'cliente_tipo')

    cliente_tipo = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Documento'}
        ),
        choices=ContaTipo.choices,
        help_text='',
        label='Tipo de Cliente',
        required=True
    )
    #queryset = User.objects().all()
    cpfcnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Documento'}
        ),
        help_text='',
        label='Documento',
        required=True
    )


    status = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': ''}
        ),
        help_text='',
        label='Documento',
        required=True
    )




    def clean(self):
        cleaned_data = super(ContaForm, self).clean()

        cpfcnpj = self.cleaned_data.get('cpfcnpj')
        tipo = self.cleaned_data.get('cliente_tipo')

        if tipo == ContaTipo.PF:
            if (len(validate_cpf(cpfcnpj))):
                raise ValidationError({'cpfcnpj': u'Cpf inválido!'})
        else:
            if (len(validate_cnpj(cpfcnpj))):
                raise ValidationError({'cpfcnpj': u'Cnpj inválido!'})

        return cleaned_data


