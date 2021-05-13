from src.tests.base import BaseCase
from flask import url_for

class TestApiVeiculos(BaseCase):
    def test_cadastrar_deve_retornar_erro_quando_o_payload_for_incompleto(self):
        dado = {
            'id':6,
            'veiculo':'Gol',
            'ano':2020,
            'descricao':'Novo'
        }

        esperado = {'marca': ['Missing data for required field.'],'vendido':['Missing data for required field.']}
        response = self.client.post(url_for('api.veiculos'), json=dado)
        response.json.pop('id')

        self.assertEqual(esperado, response.json)
