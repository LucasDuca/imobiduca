# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^$', 'views.base.index.Index', name='home'),
                       url(r'^cadastrar$', 'views.base.usuario.addusuario', name='cadastrar'),
                       url(r'^cliente/', include('django.contrib.auth.urls')),
                       url(r'^cliente/', include('urls.clientes')),
                       url(r'^imovel/', include('urls.imoveis')),

                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
