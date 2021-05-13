from typing import List
from sqlalchemy import or_
from src.db import db

class VeiculosModel(db.Model):
    __tablename__ = 'veiculos'

    id = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    vendido =  db.Column(db.Boolean, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    def __init__(self,veiculo,marca,ano,descricao,vendido,created,updated):
        self.veiculo = veiculo
        self.marca = marca
        self.ano = ano
        self.descricao = descricao
        self.vendido = vendido
        self.created = created
        self.updated = updated
    
    def __repr__(self,):
        return f'VeiculosModel(veiculo={self.vendido},marca={self.marca},{self.ano},{self.descricao},{self.vendido},{self.created},{self.updated})'

    def json(self,):
        return{
            'veiculo':self.veiculo,
            'marca':self.marca,
            'ano':self.ano,
            'descricao':self.descricao,
            'vendido':self.vendido,
            'created':self.created,
            'updated':self.updated
        }
    
    @classmethod
    def find_all(cls) -> List['VeiculosModel']:
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls,_id) -> 'VeiculosModel':
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find(cls,q) -> List['VeiculosModel']:
        search = '%{}%'.format(q)
        return cls.query.filter(or_(cls.veiculo.like(search),cls.marca.like(search),cls.descricao.like(search))).all()

    def save(self,):
        db.session.add(self)
        db.session.commit()
    
    def delete(self,):
        db.session.delete(self)
        db.session.commit()