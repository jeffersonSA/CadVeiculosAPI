from flask import Flask, Blueprint
import os
from flask_restplus import Api
from flask_cors import CORS
from src.ma import ma
from src.db import db
from marshmallow import ValidationError
class Server():
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/api/*": {"origins": "*"}})
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(
            self.bluePrint,
            version='1.0',
            title='Cadastro Veiculo API',
            description='API para cadastro de veículo',
            doc='/docs'
        )
        
        self.app.register_blueprint(self.bluePrint)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veiculo.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
    
        self.veiculos_ns = self.veiculos_ns()
        super().__init__()

    def veiculos_ns(self,):
        return self.api.namespace(name='Veiculos', description='Veiculos',path='/')

    def run(self,):
        port = int(os.environ.get("PORT", 5000))
        self.app.run(port=port, host='0.0.0.0')

server = Server()