import unittest
from src.models.cpf import CPF  # Ajuste o caminho se estiver diferente

class TestCPFService(unittest.TestCase):
    
    def test_cpf_valido(self):
        # CPF válido (gerado de forma válida): 529.982.247-25
        cpf = CPF('529.982.247-25')
        self.assertTrue(cpf.valido())

    def test_cpf_com_digitos_repetidos(self):
        # Todos os dígitos iguais (inválido)
        cpf = CPF('111.111.111-11')
        self.assertFalse(cpf.valido())

    def test_cpf_com_tamanho_invalido(self):
        # CPF com menos de 11 dígitos
        cpf = CPF('123.456.789')
        self.assertFalse(cpf.valido())

    def test_cpf_com_digitos_verificadores_errados(self):
        # CPF com dígitos finais alterados propositalmente
        cpf = CPF('529.982.247-99')  # Inválido
        self.assertFalse(cpf.valido())

    def test_cpf_formatado_com_pontos_e_traco(self):
        # Verifica se o formato não afeta a validação
        cpf = CPF('529.982.247-25')
        self.assertEqual(cpf.numero, '52998224725')
        self.assertTrue(cpf.valido())

    def test_cpf_com_caracteres_extras(self):
        cpf = CPF('  529.982.247-25\n')
        self.assertTrue(cpf.valido())

if __name__ == '__main__':
    unittest.main()
