from flask import request, jsonify
from flask_restplus import Resource, fields
from src.models.veiculos_model import VeiculosModel
from src.schemas.veiculo_schema import VeiculoSchema
from src.server.instance import server
from datetime import datetime
from marshmallow import exceptions
import json

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
        try:
            veiculo_data = VeiculosModel.find_by_id(id)
            veiculo_json = request.get_json()

            if veiculo_data:
                veiculo_data.veiculo = veiculo_json['veiculo']
                veiculo_data.marca = veiculo_json['marca']
                veiculo_data.ano = veiculo_json['ano']
                veiculo_data.descricao = veiculo_json['descricao']
                veiculo_data.vendido = veiculo_json['vendido']
                veiculo_data.updated = datetime.strptime(str(datetime.utcnow()),'%Y-%m-%d %H:%M:%S.%f')
                veiculo_data.created = datetime.strptime(str(veiculo_data.created),'%Y-%m-%d %H:%M:%S.%f')
            else:
                veiculo_data = veiculo_schema.load(veiculo_json)

            veiculo_data.save()
            return jsonify(message="Atualizado!", category="success", data=veiculo_schema.dump(veiculo_data), status=200)
        except exceptions.ValidationError as err:
            return jsonify(
                message=err.messages,
                category="error",
                status=401
            )

    @veiculos_ns.expect(item)
    def patch(self,id):
        try:
            veiculo_data = VeiculosModel.find_by_id(id)
            veiculo_json = request.get_json()
            veiculo_json['updated'] = datetime.strptime(str(datetime.utcnow()),'%Y-%m-%d %H:%M:%S.%f')
            if veiculo_data:
                if 'veiculo' in veiculo_json:
                    veiculo_data.veiculo
                
                if 'marca' in veiculo_json:
                    veiculo_data.marca = veiculo_json['marca']
                
                if 'ano' in veiculo_json:
                    veiculo_data.ano = veiculo_json['ano']

                if 'descricao' in veiculo_json:
                    veiculo_data.descricao = veiculo_json['descricao']
                
                if 'vendido' in veiculo_json:
                    veiculo_data.vendido = veiculo_json['vendido']
                    
                veiculo_data.updated = datetime.strptime(str(datetime.utcnow()),'%Y-%m-%d %H:%M:%S.%f')
                veiculo_data.created = datetime.strptime(str(veiculo_data.created),'%Y-%m-%d %H:%M:%S.%f')
            else:
                veiculo_data = veiculo_schema.load(veiculo_json)

            veiculo_data.save()
            
            return jsonify(message="Atualizado!", category="success", data=veiculo_schema.dump(veiculo_data), status=200)
        except exceptions.ValidationError as err:
            return jsonify(
                message=err.messages,
                category="error",
                status=401
            )

    def delete(self,id):
        veiculo_data = VeiculosModel.find_by_id(id)
        if veiculo_data:
            veiculo_data.delete()
            veiculo_schema.dump(veiculo_data)
            return jsonify(message="Deletado!", category="success", data=veiculo_schema.dump(veiculo_data), status=204)
        return {'message': ITEM_NOT_FOUND}, 404

class VeiculosList(Resource):
    def get(self):
        veiculo_data = VeiculosModel.find_all()
        if veiculo_data:
            return veiculo_list_schema.dump(veiculo_data), 200
        return {'message': ITEM_NOT_FOUND}, 404 
    
    @veiculos_ns.expect(item)
    @veiculos_ns.doc('Cria um novo veículo')
    def post(self):
        try:
            
            veiculo_json = request.get_data()
            if veiculo_json is None:
                return {'message': ITEM_NOT_FOUND}, 404

            veiculo_json['created'] = str(datetime.utcnow())
            veiculo_json['updated'] = str(datetime.utcnow())
            veiculo_data = veiculo_schema.load(veiculo_json)
            veiculo_data.save()
            return veiculo_schema.dump(veiculo_data), 201,{'content-type': 'application/json'}
        except exceptions.ValidationError as err:
            return jsonify(
                message=err.messages,
                category="error",
                status=401
            )
    
class VeiculosFind(Resource):
    def get(self,q):
        veiculo_data = VeiculosModel.find(q)
        if veiculo_data:
            return veiculo_list_schema.dump(veiculo_data), 200
        return {'message': 'ITEM_NOT_FOUND'}, 404   
