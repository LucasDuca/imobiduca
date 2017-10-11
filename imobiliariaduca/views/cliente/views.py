# Create your views here.
# coding: utf-8
from django.shortcuts import render


def ExibirCliente(request):

    return render(request, "cliente.html")

