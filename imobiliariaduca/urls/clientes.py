# coding: utf-8
from django.conf.urls import patterns,include, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       url(r'^$', 'views.cliente.inicio.Info', name='inicio'),


                       url(r'^casas$', 'views.cliente.views.ExibirCliente', name='casas'),
                       url(r'^apartamentos$', 'views.cliente.views.ExibirCliente', name='apartamentos'),
                       url(r'^lojas$', 'views.cliente.views.ExibirCliente', name='lojas'),
                       )
