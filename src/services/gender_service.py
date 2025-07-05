import requests
import os

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
        api_key = os.getenv('GENDER_API_KEY')
        if not api_key:
            return 'erro: token não encontrado'
        response = requests.get(f'https://gender-api.com/get?name={nome}&key={api_key}')
        if response.status_code == 200:
            return response.json().get('gender', 'desconhecido')
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
