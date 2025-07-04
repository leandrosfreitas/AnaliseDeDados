from src.services.cep_service import buscar_cep

class Endereco:
    def __init__(self, cep):
        self.cep = cep.strip()

        dados_cep = buscar_cep(self.cep)
        if cep != 'erro':
            self.bairro = dados_cep['bairro']
            self.cidade = dados_cep['cidade']
            self.estado = dados_cep['estado']
        else:
            self.bairro = self.cidade = self.estado = 'desconhecido'
