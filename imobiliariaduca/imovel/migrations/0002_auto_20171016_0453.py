# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='dono',
            field=models.ForeignKey(related_name='proprietario', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
