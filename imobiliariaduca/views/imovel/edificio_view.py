# coding: utf-8
from time import timezone

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import edit, detail, list
from django.views.generic.list import ListView

from imovel.models.edificio import Edificio
from extra_views import CreateWithInlinesView, InlineFormSet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from imovel.forms.edificio import EdificioForm
from django.db.models import Q
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import *
from imovel.choices import TipoImovel

@login_required
def Rud(request, edificio_id=None, action=None):
    template_name = 'imovel/edificio_form.html'
    success = '/imovel/sucesso'
    edificio = Edificio()

    if edificio_id:
        edificio = Edificio.objects.get(pk=edificio_id)
        form = EdificioForm(request.POST or None, instance=edificio)
    else:
        form = EdificioForm()
    if request.POST:
        if (form.is_valid()):
            edificio = form.save(commit=False)

            if action == 'create' or action == 'update':
                edificio.dono = request.user
                edificio.save()
            elif action == 'delete':
                edificio.delete()
            return HttpResponseRedirect(success)

    return render(request, template_name,
            {'edificio': edificio, 'form': form, 'action': action})



class EdificioListView(ListView):
    model = Edificio
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        usuario = self.request.user
        new_context = Edificio.objects.filter(
            Q(nome__contains=filter_val) | Q(valor__contains=filter_val) | Q(
                logradouro__contains=filter_val), dono=usuario)  # .order_by(1)

        return new_context

    def get_context_data(self, **kwargs):
        context = super(EdificioListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        # context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context


class EdificioExternoListView(ListView):
    model = Edificio
    paginate_by = 10
    template_name = 'imovel/edificioexterno_list.html'

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')

        new_context = Edificio.objects.filter(
            Q(nome__contains=filter_val) |
            Q(cidade__contains=filter_val) |
            Q(estado__contains=filter_val) |
            Q(valor__contains=filter_val), tipo=self.kwargs['tipoimovel'])  # .order_by(1)

        return new_context

    def get_context_data(self, **kwargs):
        context = super(EdificioExternoListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        # context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context


class EdificioCreateView(edit.CreateView):
    form_class = EdificioForm
    template_name = 'imovel/edificio_form.html'
    model = Edificio
    #fields = '__all__'
    fields = ['nome','image','tipo', 'status','valor', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'usuario']
    success_url = 'sucesso'

    def form_valid(self, form):
        user = self.request.user
        form.instance.dono = user
        return super(EdificioCreateView, self).form_valid(form)



class EdificioUpdateView(edit.UpdateView):
    model = Edificio
    template_name = 'imovel/edificio_form.html'
    #fields = '__all__'
    fields = ['nome','image','tipo', 'status','valor', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    success_url = 'sucesso'

class EdificioDeleteView(edit.DeleteView):
    model = Edificio
    template_name = 'imovel/edificio_form.html'
    #fields = '__all__'
    fields = ['nome','image','tipo', 'status','valor', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    success_url = 'sucesso'

def EdificioReadView(request, imovelid):
    model = Edificio.objects.filter(pk=imovelid).first()
    fields = '__all__'
    #fields = ['nome','image','tipo', 'status', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    return render(request, 'imovel/read.html', {'edificio': model})


@login_required
def EdificioListarImovel(request, imovelid):
    model = Edificio.objects.filter(pk=imovelid).first()
    fields = '__all__'
    #fields = ['nome','image','tipo', 'status', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    return render(request, 'imovel/read.html', {'edificio': model})

@login_required
def EdificioSucessoView(request):
    model = Edificio

    return render(request, 'imovel/sucesso.html', {})

