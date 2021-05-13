from flask import request
from flask_restplus import Resource, fields
from src.models.veiculos_model import VeiculosModel
from src.schemas.veiculo_schema import VeiculoSchema
from src.server.instance import server
from datetime import datetime

veiculos_ns = server.veiculos_ns
ITEM_NOT_FOUND = 'ITEM_NOT_FOUND'

item = veiculos_ns.model('Veiculos', {
   'veiculo':fields.String(),
   'marca':fields.String(),
   'ano':fields.Integer(),
   'descricao':fields.String(),
   'vendido':fields.Boolean()
})

veiculo_schema = VeiculoSchema()
veiculo_list_schema = VeiculoSchema(many=True)



class Veiculos(Resource):
    def get(self,id):
        veiculo_data = VeiculosModel.find_by_id(id)
        if veiculo_data:
            return veiculo_schema.dump(veiculo_data), 200
        return {'message': ITEM_NOT_FOUND}, 404

    @veiculos_ns.expect(item)
    def put(self,id):
        veiculo_data = VeiculosModel.find_by_id(id)
        veiculo_json = request.get_json()

        if veiculo_data:
            veiculo_data.veiculo = veiculo_json['veiculo'],
            veiculo_data.marca = veiculo_json['marca'],
            veiculo_data.ano = veiculo_json['ano'],
            veiculo_data.descricao = veiculo_json['descricao'],
            veiculo_data.vendido = veiculo_json['vendido'],
            veiculo_data.updated = datetime.now(),
        else:
            veiculo_data = veiculo_schema.load(veiculo_json)

        veiculo_data.save()
        return veiculo_schema.dump(veiculo_data), 200

    def patch(self,id):
        veiculo_data = VeiculosModel.find_by_id(id)
        veiculo_json = request.get_json()

        if veiculo_data:
            veiculo_data = veiculo_json
            veiculo_data.updated = datetime.now(),
        else:
            veiculo_data = veiculo_schema.load(veiculo_json)

        veiculo_data.save()
        return veiculo_schema.dump(veiculo_data), 200

    
    def delete(self,id):
        veiculo_data = VeiculosModel.find_by_id(id)
        if veiculo_data:
            veiculo_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

class VeiculosList(Resource):
    
    def get(self):
        veiculo_data = VeiculosModel.find_all()
        if veiculo_data:
            return veiculo_list_schema.dump(veiculo_data), 200
        return {'message': 'ITEM_NOT_FOUND'}, 404 
    
    @veiculos_ns.expect(item)
    @veiculos_ns.doc('Cria um novo veículo')
    def post(self):
        veiculo_json = request.get_json()   
       
        veiculo_json['created'] = datetime.utcnow
        veiculo_json['updated'] = datetime.utcnow
        print("JSON" + str(veiculo_json))
        veiculo_data = veiculo_schema.load(veiculo_json)
        veiculo_data.save()
        return veiculo_schema.dump(veiculo_data), 201

class VeiculosFind(Resource):
    def get(self,q):
        veiculo_data = VeiculosModel.find(q)
        if veiculo_data:
            return veiculo_list_schema.dump(veiculo_data), 200
        return {'message': 'ITEM_NOT_FOUND'}, 404   
