# coding: utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import edit, detail, list
from imovel.models.edificio import Edificio
from extra_views import CreateWithInlinesView, InlineFormSet
from django.shortcuts import render

class EdificioViewLista(list.ListView):
    template_name = 'imovel/lista.html'
#    model = Imovel

    def get_queryset(self):
        qs = super(EdificioViewLista, self).get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super(EdificioViewLista, self).get_context_data(**kwargs)

        context.update({
            'opts': context['object_list'].model._meta
        })
        return context

class EdificioViewCriar(CreateWithInlinesView):
    template_name = 'imovel/form.html'
    model = Edificio
    #fields = '__all__'
    fields = ['nome','image','tipo', 'status','valor', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    success_url = 'sucesso'

    def form_valid(self, form):
        ret = super(EdificioViewCriar,self).form_valid(form)
        messages.info(self.request, 'Imóvel %s cadastrado pelo usuário %s' % (form.instance, self.request.user.username) )


def EdificioReadView(request, imovelid):
    model = Edificio.objects.filter(pk=imovelid).first()
    fields = '__all__'
    #fields = ['nome','image','tipo', 'status', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    return render(request, 'imovel/read.html', {'edificio': model})

def EdificioSucessoView(request):
    model = Edificio

    return render(request, 'imovel/sucesso.html', {})

