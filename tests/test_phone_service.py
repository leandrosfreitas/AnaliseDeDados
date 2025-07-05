import unittest
from src.models.pessoa import Pessoa

class TestPhoneService(unittest.TestCase):

    def setUp(self):
        # Instância Pessoa com dados mínimos válidos, só para ter a instância
        self.pessoa = Pessoa(
            nome_completo="Teste",
            cpf="00000000000",  # cpf qualquer (pode ajustar)
            celular="",
            fonte="test",
            cep="00000000"  # cep qualquer, para pegar ddd = '00'
        )

    def test_format_celular_com_11_digitos(self):
        numero = "81999999999"
        esperado = "81 99999-9999"
        resultado = self.pessoa.format_celular(numero)
        self.assertEqual(resultado, esperado)

    def test_format_celular_com_10_digitos(self):
        numero = "8199999999"  # 10 dígitos
        esperado = "81 99999-9999"  # A função adiciona o 9 manualmente
        resultado = self.pessoa.format_celular(numero)
        self.assertEqual(resultado, esperado)


    def test_format_celular_com_9_digitos(self):
        numero = "999999999"
        esperado = "00 99999-9999"  # ddd usado no teste é '00'
        resultado = self.pessoa.format_celular(numero)
        self.assertEqual(resultado, esperado)

    def test_format_celular_invalido(self):
        numero = "12345"
        resultado = self.pessoa.format_celular(numero)
        self.assertEqual(resultado, numero)  # retorna o próprio valor

if __name__ == "__main__":
    unittest.main()
