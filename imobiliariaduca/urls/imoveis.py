# coding: utf-8
from django.conf.urls import patterns,include, url
from views.imovel.edificio_view import Rud,EdificioCreateView, EdificioUpdateView,EdificioExternoListView, EdificioReadView, EdificioSucessoView, EdificioListView, EdificioUpdateView
from django.contrib.auth.decorators import login_required
from imovel.choices import TipoImovel
urlpatterns = patterns('',
                       url(r'^add$', login_required(EdificioCreateView.as_view()), name='cadastrar_imovel'),
                       url(r'^update/(?P<edificio_id>[0-9]+)/$', Rud, kwargs={'action': 'update'}, name='edificio_update'),
                       url(r'^delete/(?P<edificio_id>[0-9]+)/$', Rud, kwargs={'action': 'delete'}, name='edificio_delete'),
                       url(r'^read/(?P<edificio_id>[0-9]+)/$', Rud, kwargs={'action': 'read'}, name='edificio_read'),
                       url(r'^listarimovel$', login_required(EdificioListView.as_view()), name='listar_imovel'),
                       url(r'^sucesso$', EdificioSucessoView, name='imovel_sucesso'),

                       #parte externa do site
                       url(r'^listarcasas$', EdificioExternoListView.as_view(), kwargs={'tipoimovel': TipoImovel.Casa}, name='listar_casas'),
                       url(r'^listarapartamentos$', EdificioExternoListView.as_view(), kwargs={'tipoimovel': TipoImovel.Apartamento}, name='listar_apartamentos'),
                       url(r'^listarlojas$', EdificioExternoListView.as_view(), kwargs={'tipoimovel': TipoImovel.Loja}, name='listar_lojas'),
                       url(r'^verimovel/(?P<imovelid>\d+)/$', EdificioReadView, name='ver_imovel'),



                       )

