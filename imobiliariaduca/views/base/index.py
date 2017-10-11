# coding: utf-8
from django.shortcuts import render
from imovel.models.edificio import Edificio
def Index(request):
    edificio = Edificio.objects.all()
    return render(request, "index.html", {'edificio': edificio})