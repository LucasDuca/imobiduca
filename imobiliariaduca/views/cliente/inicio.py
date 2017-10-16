# Create your views here.
# coding: utf-8
from django.shortcuts import render
from imovel.models import Edificio

def Info(request):
    cadastrados = Edificio.objects.filter(dono=request.user)
    vendas = Edificio.objects.filter(dono=request.user).exclude(usuario__isnull=True)
    compras = Edificio.objects.filter(dono=request.user, usuario=request.user)
    context = {'cadastrados': len(cadastrados),
             'vendas':len(vendas),
             'compras': len(compras)}
    return render(request, "cliente/inicio.html", context)