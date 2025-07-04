from src.services.cep_service import buscar_cep

class Endereco:
    def __init__(self, cep):
        self.cep = self.formatar_cep(cep.strip())

        dados_cep = buscar_cep(self.cep)
        if isinstance(dados_cep, dict):
            self.bairro = dados_cep.get('bairro', 'desconhecido')
            self.cidade = dados_cep.get('cidade', 'desconhecido')
            self.estado = dados_cep.get('estado', 'desconhecido')
            self.encontrado = True
        else:
            self.bairro = self.cidade = self.estado = 'desconhecido'
            self.encontrado = False

    def formatar_cep(self, cep):
        numeros = ''.join(c for c in cep if c.isdigit())
        if len(numeros) == 8:
            return f"{numeros[:5]}-{numeros[5:]}"
        return cep
