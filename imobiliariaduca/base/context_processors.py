from django.conf import settings

def geral(request):
    context = {'NOME_CLIENTE': settings.NOME_CLIENTE,
               'DESCRICAO': settings.DESCRICAO,
               'AUTOR': settings.AUTOR,
               'COPYRIGHT': settings.COPYRIGHT
               }
    return context
