# Create your views here.
# coding: utf-8
from django.shortcuts import render


def Info(request):
    return render(request, "cliente/inicio.html")