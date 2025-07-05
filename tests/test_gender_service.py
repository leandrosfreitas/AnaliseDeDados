import unittest
from unittest.mock import patch
from src.services.gender_service import usar_genderize, usar_genderapi, usar_gender_api, obter_genero

class TestGenderService(unittest.TestCase):

    @patch('src.services.gender_service.requests.get')
    def test_usar_genderize(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'gender': 'male'}
        self.assertEqual(usar_genderize('john'), 'male')

    @patch('src.services.gender_service.requests.get')
    def test_usar_genderapi(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'gender': 'female'}
        self.assertEqual(usar_genderapi('maria'), 'female')

    @patch('src.services.gender_service.requests.get')
    def test_usar_gender_api(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'gender': 'male'}
        self.assertEqual(usar_gender_api('carlos'), 'male')

    def test_obter_genero_fonte_invalida(self):
        self.assertEqual(obter_genero('ana', 'invalida'), 'Fonte inválida!')

if __name__ == '__main__':
    unittest.main()
