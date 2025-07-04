import requests

def usar_genderize(nome):
    try:
        response = requests.get(f'https://api.genderize.io?name={nome}')
        if response.status_code == 200:
            return response.json().get('gender', 'desconhecido')
    except requests.RequestException:
        pass
    return 'erro'

def usar_genderapi(nome):
    try:
        response = requests.get(f'https://api.genderapi.io/api/?name={nome}')
        if response.status_code == 200:
            return response.json().get('gender', 'desconhecido')
    except requests.RequestException:
        pass
    return 'erro'

def usar_gender_api(nome):
    try:
        reponse = requests.get(f'https://gender-api.com/get?name={nome}&key=a7def5eb0ae8f7aba44b356a432cf80fe4a758942f22b86ce6ed850948bdc0fe')
        if reponse.status_code == 200:
            return reponse.json().get('gender', 'desconhecido')
    except requests.RequestException:
        pass
    return 'erro'

def obter_genero(nome, fonte='gender_api'):
    nome = nome.strip().lower()

    if fonte == 'genderize':
        return usar_genderize(nome)
    elif fonte == 'genderapi':
        return usar_genderapi(nome)
    elif fonte == 'gender_api':
        return usar_gender_api(nome)
    else:
        return 'Fonte inválida!'
