import uuid

from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)

"""
class CategoriaTestCase(TestCase):

    def setUp(self):
        self.categoria = mommy.make('Categoria')

    def test_str(self):
        self.assertEquals(str(self.categoria), self.categoria.categoria)


class ProdutoTestCase(TestCase):

    def setUp(self):
        self.produto = mommy.make('Produto')

    def test_str(self):
        self.assertEquals(str(self.produto), self.produto.nome)
"""
