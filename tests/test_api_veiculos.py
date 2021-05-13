def test_cadastrar_deve_retornar_erro_quando_o_payload_for_incompleto(client):
    dado = {'veiculo':'Gol','ano':2020,'vendido':True}
    esperado = {'marca': ['Missing data for required field.'], 'descricao': ['Missing data for required field.']}
    response = client.post('/api/veiculos',json=dado)
    assert response.json == esperado