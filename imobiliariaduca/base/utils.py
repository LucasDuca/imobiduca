# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import EMPTY_VALUES

import re
def validate_cpf(value):
    """
    CPF validation for Django fields.
    """
    default_error_messages = {
        'invalid_cpf': u"Número de CPF inválido.",
        'max_digits_cpf': u"O CPF deve conter 11 dígitos.",
        'digits_only': u"Digíte apenas os números.",
    }
    errors = []
    def checksum(v):
        if v >= 2:
            return 11 - v
        return 0

    if value in EMPTY_VALUES:
        errors.append(default_error_messages['invalid_cpf'])
        return errors

    if not value.isdigit():
        value = re.sub('[-\.]', '', value)
    orig_value = value[:]

    # special cases
    if '22222222222' == value:
        errors.append(default_error_messages['invalid_cpf'])
        return errors
    if '00000000000' == value:
        errors.append(default_error_messages['invalid_cpf'])
        return errors
    if '99999999999' == value:
        errors.append(default_error_messages['invalid_cpf'])
        return errors

    try:
        int(value)
    except ValueError:
        errors.append(default_error_messages['digits_only'])
        return errors

    if len(value) != 11:
        errors.append(default_error_messages['max_digits_cpf'])
        return errors
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = checksum(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = checksum(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        errors.append(default_error_messages['invalid_cpf'])
        return errors

    return errors


def validate_cnpj(cnpj):
     """
     Valida CNPJs, retornando apenas a string de números válida.
     """
     cnpj = ''.join(re.findall('\d', str(cnpj)))
     errors = []
     if (not cnpj) or (len(cnpj) < 14):
         errors.append(u"Número de caracteres menor que o esperado.")
         return errors

     # special cases
     if '00000000000000' == cnpj:
         errors.append(u"CNPJ inválido.")
         return errors

     # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
     inteiros = map(int, cnpj)
     novo = inteiros[:12]

     prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
     while len(novo) < 14:
         r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
         if r > 1:
             f = 11 - r
         else:
             f = 0
         novo.append(f)
         prod.insert(0, 6)

     # Se o número gerado coincidir com o número original, é válido
     if novo != inteiros:
         errors.append(u"CNPJ inválido.")
         return errors
     return errors