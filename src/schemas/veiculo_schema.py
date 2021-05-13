from flask_sqlalchemy import model
from src.ma import ma
from src.models.veiculos_model import VeiculosModel

class VeiculoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VeiculosModel