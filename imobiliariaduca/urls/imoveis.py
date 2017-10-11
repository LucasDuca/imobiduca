# coding: utf-8
from django.conf.urls import patterns,include, url
from views.imovel.edificio_view import EdificioViewCriar, EdificioReadView, EdificioSucessoView

urlpatterns = patterns('',
                       url(r'^cadastrarimovel$', EdificioViewCriar.as_view(), name='cadastrar_imovel'),
                       url(r'^sucesso$', EdificioSucessoView, name='imovel_sucesso'),
                       url(r'^verimovel/(?P<imovelid>\d+)/$', EdificioReadView, name='ver_imovel'),
                       #url(r'^alterarimovel$', 'cliente.views.views.CadastrarImovel', name='alterar_imovel'),
                       #url(r'^excluirimovel$', 'cliente.views.views.CadastrarImovel', name='excluir_imovel'),



                       )
