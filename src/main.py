from src.models.pessoa import Pessoa

if __name__ == '__main__':
    pessoa = Pessoa('Maria Lucia', '103.477.004-70', '81992915316', 'genderize', '50630610')
    print(pessoa.nome_completo)
    print(pessoa.cpf.numero)
    print(pessoa.cpf.valido())
    print(pessoa.primeiro_nome)
    print(pessoa.segundo_nome)
    print(pessoa.celular)
    print(pessoa.genero)
    print(pessoa.endereco.bairro)
    print(pessoa.endereco.cidade)
    print(pessoa.endereco.estado)
