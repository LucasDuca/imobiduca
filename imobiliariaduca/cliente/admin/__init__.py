# coding: utf-8
from django.contrib import admin
from django.contrib.admin import site

from cliente.admin.conta import ContaAdmin
from cliente.models.conta import Conta



admin.site.register(Conta, ContaAdmin)

admin.site.disable_action('delete_selected')

import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)