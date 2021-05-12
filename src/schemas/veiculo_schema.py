from flask_sqlalchemy import model
from ma import ma
from models.veiculos_model import VeiculosModel

class VeiculoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VeiculosModel
        load_instance  = True