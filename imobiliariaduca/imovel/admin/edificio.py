# Register your models here.
# coding: utf-8
from django.contrib import admin
from imovel.models.edificio import Edificio

class EdificioAdmin(admin.ModelAdmin):
    search_fields = ('nome','status',
                     'bairro', 'cidade', 'estado')
    list_display = ('image_tag', 'nome','valor', 'status', 'logradouro','complemento','bairro', 'cidade', 'estado')
    fields = ('image_tag', 'nome', 'valor','status',
                     'logradouro','complemento','bairro', 'cidade', 'estado')



    def __init__(self, *args, **kwargs):
        super(EdificioAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

    def has_add_permission(self, request):
        return False
