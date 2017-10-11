# Register your models here.
# coding: utf-8
from django.contrib import admin
from cliente.models.conta import Conta

class ContaAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nome','status')
    list_display = ('id', 'nome','status')
    #list_filter = ('status')
    #readonly_fields = ('status_formatado',)
    #filter_horizontal = ('grupo_pessoa','grupo', 'grupo_flex')

