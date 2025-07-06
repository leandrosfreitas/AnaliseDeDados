# Análise de Dados de Pessoas - Projeto Python

## Descrição

Este projeto é uma aplicação Python para manipulação, validação e análise de dados pessoais extraídos de arquivos CSV contendo informações como nome completo, CPF, telefone, CEP, e-mail e áreas de interesse.

A aplicação realiza as seguintes funções principais:

- **Validação de CPF**: Verifica a validade dos números de CPF informados.
- **Consulta e preenchimento de endereço pelo CEP**: Obtém dados de endereço (bairro, cidade, estado, DDD) consultando a API ViaCEP.
- **Formatação e validação de números de telefone celular**.
- **Identificação de gênero** por meio de APIs externas (Genderize, GenderAPI, Gender API), com escolha da fonte pelo usuário.
- **Exportação dos dados processados** em formatos CSV e JSON.
- **Geração de relatório analítico** com informações sobre:
  - Distribuição de gênero
  - Distribuição geográfica por estado
  - Qualidade dos dados (CPFs inválidos, telefones ausentes)
  - Percentual geral por área de interesse
  - Áreas de interesse segmentadas por gênero

## Estrutura do Projeto

```
src/
  models/
    cpf.py
    endereco.py
    pessoa.py
  repo/
    csv_repo.py
    json_repo.py
    relatorio_repo.py
    lista_clientes_saida.csv   # Arquivo CSV gerado pela aplicação
    lista_clientes_saida.json  # Arquivo JSON gerado pela aplicação
  services/
    cep_service.py
    gender_service.py
  main.py
tests/
  test_cpf_service.py
  test_gebder_service.py
  test_phone_service.py
lista_clientes.csv         # Arquivo CSV de entrada com dados dos clientes
.gitignore
README.md
```

## Como usar

1. **Pré-requisitos**

- Python 3.x instalado
- Biblioteca `requests` instalada (`pip install requests`)

2. **Configuração**

- Se desejar usar a API Gender API que requer token, configure a variável de ambiente `GENDER_API_KEY`.

3. **Execução**

- Coloque seu arquivo `lista_clientes.csv` na raiz do projeto (ou ajuste o caminho no código).
- Execute o script principal:

```bash
python src/main.py
```

- Quando solicitado, informe qual API usar para obter o gênero: `genderize`, `genderapi` ou `gender_api`.

4. **Saídas**

- O programa gera arquivos `lista_clientes_saida.csv` e `lista_clientes_saida.json` na pasta `src/repo/`.
- Exibe um relatório analítico no console com diversas informações sobre os dados processados.

## Formato esperado do CSV de entrada

O arquivo CSV deve conter as colunas (nomes exatos):

- `NomeCompleto`
- `CPF`
- `Celular`
- `CEP`
- `Email`
- `Interesse`

## Testes

Na pasta `tests/` estão implementados testes unitários para as principais funcionalidades do projeto, garantindo qualidade e confiabilidade do código.

Para rodar os testes, utilize:

```bash
python -m unittest discover tests
```

## Tecnologias e APIs utilizadas

- Python 3.x
- Biblioteca `requests` para chamadas HTTP
- API ViaCEP para consulta de dados de endereço pelo CEP
- APIs para determinação de gênero por nome:
  - Genderize.io
  - GenderAPI.io
  - Gender API (requere token)
