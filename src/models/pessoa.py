from .cpf import CPF
from src.services.gender_service import obter_genero
from .endereco import Endereco

class Pessoa():
    def __init__(self, nome_completo, cpf, celular, fonte, cep):
        self.nome_completo = nome_completo.strip()
        self.cpf = CPF(cpf)
        self.celular = celular.strip()
        nomes = self.nome_completo.split()
        self.primeiro_nome = nomes[0].strip()
        self.segundo_nome = self.extrairSegundoNome(nomes)
        self.genero = obter_genero(self.primeiro_nome, fonte)
        
        self.endereco = Endereco(cep)

        self.observacoes = []

    def extrairSegundoNome(self, nomes):
        preposicoes = {"de", "da", "do", "das", "dos"}
        if len(nomes) >= 3 and nomes[1].lower() in preposicoes:
            return f"{nomes[1]} {nomes[2]}"
        elif len(nomes) >= 2:
            return nomes[1]
        return ""
