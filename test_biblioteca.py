import os
import unittest
import tempfile
import shutil
from biblioteca import listar_documentos, adicionar_documento, renomear_documento, remover_documento

class TestBibliotecaDigital(unittest.TestCase):

    def setUp(self):
        """Cria um diretorio temporario para os testes."""
        self.test_dir = tempfile.mkdtemp()
        # Criar arquivos de teste
        open(os.path.join(self.test_dir, 'artigo_2023.pdf'), 'w').close()
        open(os.path.join(self.test_dir, 'tese_2022.pdf'), 'w').close()
        open(os.path.join(self.test_dir, 'livro.epub'), 'w').close()
        open(os.path.join(self.test_dir, 'notas.txt'), 'w').close()

    def tearDown(self):
        """Remove o diretorio temporario apos cada teste."""
        shutil.rmtree(self.test_dir)

    def test_listar_por_tipo(self):
        """Testa se a listagem por tipo funciona corretamente."""
        por_tipo, _ = listar_documentos(self.test_dir)
        self.assertIn('.pdf', por_tipo)
        self.assertIn('.epub', por_tipo)
        self.assertEqual(len(por_tipo['.pdf']), 2)
        self.assertEqual(len(por_tipo['.epub']), 1)
        print("PASSOU: Listagem por tipo")

    def test_listar_por_ano(self):
        """Testa se a listagem por ano funciona corretamente."""
        _, por_ano = listar_documentos(self.test_dir)
        self.assertTrue(len(por_ano) > 0)
        print("PASSOU: Listagem por ano")

    def test_adicionar_documento(self):
        """Testa adicao de documento valido."""
        arquivo_origem = os.path.join(self.test_dir, 'novo_artigo.pdf')
        open(arquivo_origem, 'w').close()
        destino = tempfile.mkdtemp()
        resultado = adicionar_documento(arquivo_origem, destino)
        self.assertTrue(resultado)
        self.assertTrue(os.path.exists(os.path.join(destino, 'novo_artigo.pdf')))
        shutil.rmtree(destino)
        print("PASSOU: Adicao de documento")

    def test_adicionar_extensao_invalida(self):
        """Testa que extensoes invalidas sao rejeitadas."""
        arquivo = os.path.join(self.test_dir, 'planilha.xlsx')
        open(arquivo, 'w').close()
        resultado = adicionar_documento(arquivo, self.test_dir)
        self.assertFalse(resultado)
        print("PASSOU: Rejeicao de extensao invalida")

    def test_renomear_documento(self):
        """Testa renomeacao de documento."""
        resultado = renomear_documento('artigo_2023.pdf', 'artigo_renomeado.pdf', self.test_dir)
        self.assertTrue(resultado)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'artigo_renomeado.pdf')))
        print("PASSOU: Renomeacao de documento")

    def test_renomear_inexistente(self):
        """Testa renomeacao de arquivo que nao existe."""
        resultado = renomear_documento('nao_existe.pdf', 'novo.pdf', self.test_dir)
        self.assertFalse(resultado)
        print("PASSOU: Erro ao renomear inexistente")

    def test_remover_documento(self):
        """Testa remocao de documento."""
        resultado = remover_documento('notas.txt', self.test_dir)
        self.assertTrue(resultado)
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'notas.txt')))
        print("PASSOU: Remocao de documento")

    def test_remover_inexistente(self):
        """Testa remocao de arquivo que nao existe."""
        resultado = remover_documento('nao_existe.pdf', self.test_dir)
        self.assertFalse(resultado)
        print("PASSOU: Erro ao remover inexistente")

if __name__ == '__main__':
    print("Executando testes do Sistema de Biblioteca Digital...\n")
    unittest.main(verbosity=2)
