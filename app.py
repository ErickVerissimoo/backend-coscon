from flask import request, jsonify
from models.classes import *
from models.database import *
import json
app = create_app()

@app.route('/api/cadastro', methods=['POST'])
def cadastrar(): 
    data = request.json
    addUser(data.get('username'), data.get('email'),  data.get('password'))
    return jsonify({"Mensagem": "usuario cadastrado com sucesso!"})


@app.route('/api/comentar')
def comentar():
    data = request.json
    


@app.route('/api/feed', methods =['GET'] )
def feed():
    return json.dumps(getFeed())

if __name__=='__main__':
    app.run(debug=True)