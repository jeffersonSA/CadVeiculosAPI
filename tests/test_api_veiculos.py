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

    dado = {
        'veiculo':'Golzinho',
        'ano':2001,
        'vendido':False,
        'marca': 'VWs', 
        'descricao': 'seminovo'
    }

    response = client.put('/api/veiculos/%s' % id,json=dado)
    data_resp = response.get_json()['data']
    del data_resp['created'], data_resp['updated'], data_resp['id']

    assert data_resp == dado

def test_patch_deve_atualizar_somente_atributo_vendido(client):
    dado = {
        'veiculo':'Audi',
        'ano':2020,
        'vendido':False,
        'marca': 'Audi', 
        'descricao': 'Novo'
    }

    response = client.post('/api/veiculos',json=dado)
    resp_json = response.get_json()
    id = resp_json['id']

    dado = {
        'vendido':False
    }

    response = client.patch('/api/veiculos/%s' % id,json=dado)
    data_resp = response.get_json()['data']
    assert data_resp['vendido'] == False

def test_delete_deve_mostrar_mensagem_deletado_ao_deleltar(client):
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

    response = client.delete('/api/veiculos/%s' % id)
    assert response.get_json()['message'] == "Deletado!"