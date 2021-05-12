from db import db
from ma import ma
from marshmallow import ValidationError
from server.instance import server
from resources.veiculos import Veiculos, VeiculosList, VeiculosFind

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Veiculos,'/veiculos/<int:id>')
api.add_resource(VeiculosList,'/veiculos')
api.add_resource(VeiculosFind,'/veiculos/find/<string:q>')
db.init_app(app)
if __name__ == '__main__':
    ma.init_app(app)
    server.run()