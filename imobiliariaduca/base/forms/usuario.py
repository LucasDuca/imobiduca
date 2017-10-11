# coding: utf-8
from django.contrib.auth.models import User
from django import forms
from suit.widgets import NumberInput, HTML5Input, TextInput

from django.core.exceptions import ValidationError

class UsuarioForm(forms.Form):
    model = User
    objects = User.objects

    fields = ('username', 'email', 'password')

    #queryset = User.objects().all()
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome do Usuário'}
        ),
        help_text='',
        label='Usuário',
        required=True
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'E-mail'}
        ),
        help_text='',
        label='E-mail',
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',   'placeholder': 'Senha'}
        ),
        help_text='',
        label='Senha',
        required=True
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError(u'E-mail %s já esta registrado. Faça Login ou utilize outro e-mail.' % email)


    def clean_username(self):
        nome = self.cleaned_data.get('username')
        usuario = User.objects.filter(username=nome).first()
        if usuario:
            raise ValidationError(u'O usuário %s já existe' % nome)
        return nome

