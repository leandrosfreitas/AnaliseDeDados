import re
from .cpf import CPF
from src.services.gender_service import obter_genero
from .endereco import Endereco

class Pessoa():
    def __init__(self, nome_completo, cpf, celular, fonte, cep):
        self.nome_completo = nome_completo.strip()
        self.cpf = CPF(cpf)
        self.endereco = Endereco(cep)
        self.celular = self.format_celular(celular)
        nomes = self.nome_completo.split()
        self.primeiro_nome = nomes[0].strip()
        self.segundo_nome = self.extrairSegundoNome(nomes)
        self.genero = obter_genero(self.primeiro_nome, fonte)
        self.observacoes = []

        valido_cpf = self.cpf.valido()
        if valido_cpf != True:
            self.observacoes.append(f"CPF inválido")
        
        if not self.endereco.encontrado:
            self.observacoes.append("CEP inválido ou não encontrado.")
        
        if not celular or not celular.strip():
            self.observacoes.append("Telefone ausente.")
        elif not self.celular_valido(self.celular):
            self.observacoes.append("Telefone inválido. Formato esperado: 'DD 9XXXX-XXXX'.")

    def extrairSegundoNome(self, nomes):
        preposicoes = {"de", "da", "do", "das", "dos"}
        if len(nomes) >= 3 and nomes[1].lower() in preposicoes:
            return f"{nomes[1]} {nomes[2]}"
        elif len(nomes) >= 2:
            return nomes[1]
        return ""
    
    def celular_valido(self, celular):
        padrao = r'^\d{2}\s9\d{4}-\d{4}$'
        return re.match(padrao, celular)
    
    def format_celular(self, celular):
        numeros = ''.join(c for c in celular if c.isdigit())
        ddd = self.endereco.ddd
        if not ddd or not ddd.isdigit() or len(ddd) != 2:
            ddd = '00'

        if len(numeros) == 11:
            return f'{numeros[:2]} {numeros[2:7]}-{numeros[7:]}'
        elif len(numeros) == 10:
            return f'{numeros[:2]} 9{numeros[2:6]}-{numeros[6:]}'
        elif len(numeros) == 9:
            return f'{ddd} {numeros[:5]}-{numeros[5:]}'
        elif len(numeros) == 8:
            return f'{ddd} 9{numeros[:4]}-{numeros[4:]}'
        else:
            return celular
    
    def to_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "primeiro_nome": self.primeiro_nome,
            "segundo_nome": self.segundo_nome,
            "genero": self.genero,
            "cpf": self.cpf.numero,
            "celular": self.celular,
            "cep": self.endereco.cep,
            "bairro": self.endereco.bairro,
            "cidade": self.endereco.cidade,
            "estado": self.endereco.estado,
            "observacoes": '; '.join(self.observacoes),
            "email": getattr(self, "email", ""),
            "interesse": getattr(self, "interesse", "")
        }
