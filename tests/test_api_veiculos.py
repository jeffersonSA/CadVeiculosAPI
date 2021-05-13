import json
def test_post_deve_retornar_erro_quando_o_payload_for_incompleto(client):
    dado = {'veiculo':'Gol','ano':2020,'vendido':True}
    esperado = {'marca': ['Missing data for required field.'], 'descricao': ['Missing data for required field.']}
    
    response = client.post('/api/veiculos',json=dado)
    assert response.get_json()['message'] == esperado

def test_post_deve_retornar_erro_quando_o_payload_contiver_a_chave_id(client):
    dado = {
        'veiculo':'Gol',
        'ano':2020,
        'vendido':True,
        'marca': 'VW', 
        'descricao': 'Novo',
        'id': 1
    }

    esperado =  {'id': ['Não é permitido enviar ID']}
    response = client.post('/api/veiculos',json=dado)

    assert response.get_json()['message'] == esperado

def test_get_deve_retornar_status_200(client):
    assert client.get('/api/veiculos').status_code == 200

def test_get_deve_retornar_dado_depois_de_inserir(client):
    dado = {
        'veiculo':'Gol',
        'ano':2020,
        'vendido':True,
        'marca': 'VW', 
        'descricao': 'Novo'
    }

    response = client.post('/api/veiculos',json=dado)
    resp_json = response.get_json()
   
    id = resp_json['id']

    esperado = resp_json
    response = client.get('/api/veiculos/%s' %id )
    assert response.get_json() == esperado

def test_get_deve_retornar_dados_usando_qualquer_texto_digitado(client):
    
    dado = [{
        'veiculo':'Celta',
        'ano':1990,
        'vendido':True,
        'marca': 'GM', 
        'descricao': 'Antigo'
    },
    {
        'veiculo':'Corsa',
        'ano':1990,
        'vendido':True,
        'marca': 'GM', 
        'descricao': 'Antigo'
    },
    {
        'veiculo':'Gol',
        'ano':2021,
        'vendido':True,
        'marca': 'VW', 
        'descricao': 'Novo'
    }]

    client.post('/api/veiculos',json=dado[0])
    client.post('/api/veiculos',json=dado[1])
    client.post('/api/veiculos',json=dado[2])
    sarch_word = 'Anti'
 
    response = client.get('/api/veiculos/find/%s' % sarch_word)

    assert len(response.get_json()) >=2 

def test_put_deve_atualizar_dado_adicionado(client):
    ...

def test_patch_deve_atualizar_somente_marca(client):
    ...

def test_deve_deletar(client):
    ...