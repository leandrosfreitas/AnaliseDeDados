import json

def exportar_pessoas_para_json(pessoas, caminho_arquivo):
    pessoas_ordenadas = sorted(pessoas, key=lambda p: p.nome_completo.lower())
    usuarios = [p.to_dict() for p in pessoas_ordenadas]

    dados = {
        "users": usuarios
    }

    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
