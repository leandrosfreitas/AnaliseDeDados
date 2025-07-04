class CPF:
    def __init__(self, numero):
        self.numero = self._somente_digitos(numero)

    def _somente_digitos(self, cpf):
        return ''.join(d for d in cpf if d.isdigit())
    
    def valido(self):
        cpf = self.numero

        if len(cpf) != 11:
            return False
        
        if cpf == cpf[0] * 11:
            return False
        
        # Valida 1º dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10) % 11
        if digito1 == 10:
            digito1 = 0
        if digito1 != int(cpf[9]):
            return False

        # Valida 2º dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10) % 11
        if digito2 == 10:
            digito2 = 0
        if digito2 != int(cpf[10]):
            return False

        return True
