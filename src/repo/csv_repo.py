import csv

def exportar_pessoas_para_csv(pessoas, caminho_arquivo):
    if not pessoas:
        return
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as f:
        fieldnames = list(pessoas[0].to_dict().keys())
        fieldnames.extend(['email', 'interesse'])
        fieldnames = list(dict.fromkeys(fieldnames))

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for p in pessoas:
            linha = p.to_dict()
            linha['email'] = getattr(p, 'email', '')
            linha['interesse'] = getattr(p, 'interesse', '')
            writer.writerow(linha)
