import datetime
from django import test
from imovel.models.edificio import Edificio
from django.contrib.auth.models import User
from imovel.choices import TipoImovel, StatusVenda,ESTADOS
from imovel.forms.edificio import EdificioForm
from django.core.files.uploadedfile import SimpleUploadedFile

class EdificioTests(test.TestCase):

    def setUp(self):
        usuario = User.objects.create_superuser('teste@example.com', 'teste', 'teste')

        from django.core.files.uploadedfile import SimpleUploadedFile

        img = open('imovel/static/teste_image.jpg')
        uploaded = SimpleUploadedFile(img.name, img.read())
        files = {'image': uploaded}

        self.data = dict(
        nome = 'Teste',
        tipo = TipoImovel.Casa,
        status = StatusVenda.Aguardando,
        valor = 100.00,

        usuario = usuario.id,

        logradouro = 'logradouro',
        numero = 100,
        complemento = 'complemento',
        bairro = 'bairro',
        cidade = 'Rio de Janeiro',
        estado = 'RJ',
        cep = '25545201',


        )

        self.form = EdificioForm(self.data, files)

        #super(Edificio, self).setUp()

    def test_cria_Edificio(self):
        is_valid = self.form.is_valid()

        self.assertTrue(is_valid, True)

        self.form.save()

        self.assertEqual(1, Edificio.objects.count())
        edificio_criado = Edificio.objects.first()

        self.assertEqual(edificio_criado.nome, 'Teste')
        self.assertEqual(edificio_criado.tipo, TipoImovel.Casa)
        self.assertEqual(edificio_criado.status, StatusVenda.Aguardando)

        self.assertEqual(edificio_criado.valor, 100.00)

        self.assertEqual(edificio_criado.nome, 'Teste')

        usuario = User.objects.first()
        self.assertIsNotNone(edificio_criado.usuario.id)


        self.assertEqual(edificio_criado.logradouro, 'logradouro')
        self.assertEqual(edificio_criado.numero, 100)

        self.assertEqual(edificio_criado.complemento, 'complemento')
        self.assertEqual(edificio_criado.bairro, 'bairro')
        self.assertEqual(edificio_criado.cidade, 'Rio de Janeiro')
        self.assertEqual(edificio_criado.estado, 'RJ')
        self.assertEqual(edificio_criado.cep, '25545201')


