# coding: utf-8
from base.forms.usuario import UsuarioForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.shortcuts import render
from cliente.models.conta import Conta
from cliente.forms.conta import ContaForm

def addusuario(request):

    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            #conta = Conta
            new_user = UsuarioForm.objects.create_user(**form.cleaned_data)
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            #conta.nome = form.cleaned_data.get('nome')

            login(request, new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('cliente/')
    else:
        form = UsuarioForm

    return render(request, 'cadastro/addusuario.html', {'form': form})