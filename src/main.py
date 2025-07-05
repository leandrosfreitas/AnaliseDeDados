from src.models.pessoa import Pessoa
from src.repo.csv_repo import exportar_pessoas_para_csv
from src.repo.json_repo import exportar_pessoas_para_json
from src.repo.relatorio_repo import gerar_relatorio
import csv

def ler_pessoas_csv(caminho_arquivo, fonte_genero):
    pessoas = []
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pessoa = Pessoa(
                nome_completo=row.get('NomeCompleto', '').strip(),
                cpf=row.get('CPF', '').strip(),
                celular=row.get('Celular', '').strip(),
                fonte=fonte_genero.strip().lower(),
                cep=row.get('CEP', '').strip()
            )
            pessoa.email = row.get('Email', '').strip()
            pessoa.interesse = row.get('Interesse', '').strip()
            pessoas.append(pessoa)

    return pessoas

def main():
    fonte = input("Informa a API de gênero: genderize | genderapi | gender_api: ").strip().lower()

    if fonte not in ['genderize', 'genderapi', 'gender_api']:
        print("Fonte inválida. Usando 'genderize' como padrão.")
        fonte = 'genderize'

    pessoas = ler_pessoas_csv('lista_clientes.csv', fonte)

    exportar_pessoas_para_csv(pessoas, 'src/repo/lista_clientes_saida.csv')
    exportar_pessoas_para_json(pessoas, 'src/repo/lista_clientes_saida.json')

    gerar_relatorio(pessoas)

if __name__ == '__main__':
    main()
