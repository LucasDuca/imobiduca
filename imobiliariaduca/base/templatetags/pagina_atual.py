# coding: utf-8
from django import template
from django.core.urlresolvers import reverse
register = template.Library()


@register.simple_tag
def eh_atual(request, url, css_class='active'):
    if url[0] == '/':
        if request.path == url:
            return css_class
    else:
        if request.path == reverse(url):
            return "active"

    return ""


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})