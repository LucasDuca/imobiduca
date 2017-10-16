# coding: utf-8
from django.contrib import admin
from django.contrib.admin import site

from imovel.admin.edificio import EdificioAdmin
from imovel.models.edificio import Edificio



admin.site.register(Edificio, EdificioAdmin)

#admin.site.disable_action('update_selected')
#admin.site.disable_action('delete_selected')

import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)