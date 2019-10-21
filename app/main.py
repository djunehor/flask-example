
from flask import Flask, jsonify
from flask_restplus import Resource, Api, Namespace
from mysql_db import MysqlDb

db = MysqlDb()
app = Flask(__name__)
api = Api(app)

gene = Namespace('genes', description='Search for gene in ensembl database')
api.add_namespace(gene)


# Create a REST resource
@gene.route('/<string:name>')
@gene.route('/<string:name>/<string:species>')
class Gene(Resource):
    def get(self, name, species=None):
        return jsonify(db.search({'name' : name, 'species': species}))


if __name__ == '__main__':
    app.run(debug=True)
