import requests

def buscar_cep(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            return {
                'bairro': dados.get('bairro'),
                'cidade': dados.get('localidade'),
                'estado': dados.get('uf')
            }
    except:
        pass
    return 'erro'
