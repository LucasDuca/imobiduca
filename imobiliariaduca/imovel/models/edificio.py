# coding: utf-8
from django.db import models
from imovel.choices import TipoImovel, StatusVenda
from django.contrib.gis.db import models as models_gis
from imovel.choices import ESTADOS
from django.contrib.auth.models import User
from django.db import connection
from collections import namedtuple

class Edificio(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=55)
    dono = models.OneToOneField(User, null=True, blank=True, related_name='proprietario')
    image = models.ImageField(upload_to='imovel/images', verbose_name='Imagens')
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    usuario = models.ForeignKey(User, null=True, blank=True)
    tipo = models.CharField(
        max_length=20, choices=TipoImovel.choices, null=False, blank=False,
        verbose_name="Tipo de Imóvel",
        help_text="Tipo de Imóvel."
    )

    status = models.CharField(
        max_length=20, choices=StatusVenda.choices, default=StatusVenda.Aguardando, blank=False,
        verbose_name="Status da Venda",
        help_text="Status da Venda do Imóvel."
    )

    data_cadastro = models.DateTimeField(
        verbose_name="Data de cadastro", auto_now_add=True,
        help_text="Data em que foi cadastrado o imóvel."
    )

    logradouro = models.CharField(max_length=255, null=False, blank=False)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    cidade = models.CharField(max_length=30, default="Rio de Janeiro", null=False, blank=False)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='RJ', null=False, blank=False)
    cep = models.CharField(max_length=9, null=False, blank=False)





    def __str__(self):
        return "%s - %s " % (self.nome, self.dono)

    def Meta(self):
        verbose_name = 'Edificio'
        verbose_name_plural = 'Edificios'

    def get_image(self, edificio):
        if edificio.image and hasattr(edificio.image, 'url'):
            protocol = 'https://' if self.request.is_secure() else 'http://'
            return '%s%s%s' % (protocol, self.request.META['HTTP_HOST'],edificio.image.url)

        return None
    def pontos_por_itinerario(lat, lng, distancia):
        try:
            latitude = float(lat)
            longitude = float(lng)
        except:
            return []

        query = """
          WITH pontos_proximos AS (
              SELECT
                id AS casa_id,
                coordenada,
                ST_Distance(coordenada, ST_GeomFromText('POINT(%s %s)', 4326), TRUE) AS distancia,
                logradouro||', '||numero as endereco
              FROM imovel_edificio  
          )
          SELECT
            px.distancia AS distancia,
            px.casa_id,
            ST_X(px.coordenada) as ponto_x,
            ST_Y(px.coordenada) as ponto_y,
            px.endereco

          FROM pontos_proximos px
            WHERE px.distancia < %s
          ORDER BY distancia
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [latitude, longitude, distancia])

            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            return [nt_result(*row) for row in cursor.fetchall()]


