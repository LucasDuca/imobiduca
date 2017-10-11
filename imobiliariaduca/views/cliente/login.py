# Create your views here.
# coding: utf-8
from django.views.generic import detail

from views.base.view import LoginRequiredMixin


class LoginView(LoginRequiredMixin, detail.DetailView):
    template_name = 'cliente/inicio.html'

    def get_object(self, queryset=None):
        print('>>>>>>>>>>', self.request.user, '<<<<<<<<<<<<')
        #pessoa = self.request.user.pessoa
        #return pessoa.passe_set.unico_ativo()
        return True
