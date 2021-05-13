from flask_sqlalchemy import model
from src.ma import ma
from src.models.veiculos_model import VeiculosModel
from marshmallow import validates, ValidationError

class VeiculoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VeiculosModel
        load_instance  = True
    
    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não é permitido enviar ID')