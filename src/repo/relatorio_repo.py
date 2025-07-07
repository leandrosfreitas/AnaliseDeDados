from collections import Counter, defaultdict

def validar_cpf(cpf_obj):
    return cpf_obj.valido()

def gerar_relatorio(pessoas):
    total = len(pessoas)
    if total == 0:
        print("Nenhuma pessoa para analisar.")
        return

    print("\n=== RELATÓRIO ANALÍTICO ===")

    # 1. Distribuição de gênero
    generos = [p.genero for p in pessoas]
    cont_genero = Counter(generos)

    homens = cont_genero.get('male', 0)
    mulheres = cont_genero.get('female', 0)
    outros = total - homens - mulheres

    print("\n→ Distribuição de Gênero:")
    print(f"  Homens: {homens} ({(homens/total)*100:.2f}%)")
    print(f"  Mulheres: {mulheres} ({(mulheres/total)*100:.2f}%)")
    print(f"  Desconhecido/Outro: {outros} ({(outros/total)*100:.2f}%)")

    # 2. Distribuição geográfica (por estado)
    estados_para_regioes = {
        # Norte
        'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte',
        'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',

        # Nordeste
        'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste',
        'PB': 'Nordeste', 'PE': 'Nordeste', 'PI': 'Nordeste',
        'RN': 'Nordeste', 'SE': 'Nordeste',

        # Centro-Oeste
        'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',

        # Sudeste
        'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',

        # Sul
        'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul',
    }

    estados = [p.endereco.estado for p in pessoas]
    regioes = [estados_para_regioes.get(estado, 'Desconhecido') for estado in estados]
    cont_regioes = Counter(regioes)

    print("\n→ Distribuição Geográfica (por região):")
    for regiao, qtd in cont_regioes.items():
        print(f"  {regiao}: {qtd} ({(qtd/total)*100:.2f}%)")

    # 3. Qualidade dos dados
    cpfs_invalidos = [p for p in pessoas if not validar_cpf(p.cpf)]
    celulares_ausentes = [p for p in pessoas if not p.celular.strip()]

    pessoas_com_erro = set(cpfs_invalidos + celulares_ausentes)

    print("\n→ Qualidade dos Dados:")
    print(f"  Pessoas com erro de qualidade: {len(pessoas_com_erro)} ({(len(pessoas_com_erro)/total)*100:.2f}%)")
    print(f"    - CPFs inválidos: {len(cpfs_invalidos)}")
    print(f"    - Celulares ausentes: {len(celulares_ausentes)}")

    # 4. Percentual das áreas de interesse (geral)
    interesses = [p.interesse for p in pessoas if p.interesse]
    cont_interesses = Counter(interesses)
    total_interesses = sum(cont_interesses.values())

    print("\n→ Percentual Geral por Área de Interesse:")
    for area, qtd in cont_interesses.items():
        print(f"  {area}: {qtd} ({(qtd/total_interesses)*100:.2f}%)")

    # 5. Áreas de interesse por gênero
    interesses_por_genero = defaultdict(Counter)
    for p in pessoas:
        if p.interesse:
            genero = p.genero.lower() if p.genero and p.genero.lower() in ('male', 'female') else 'desconhecido'
            interesses_por_genero[genero][p.interesse] += 1

    print("\n→ Áreas de Interesse por Gênero:")
    for genero, cont in interesses_por_genero.items():
        total_genero = sum(cont.values())
        print(f"  {genero.capitalize()}:")
        for area, qtd in cont.items():
            print(f"    {area}: {qtd} ({(qtd/total_genero)*100:.2f}%)")

    print("\n=== FIM DO RELATÓRIO ===\n")
