from flask import request, jsonify, make_response, session
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
    
@app.route('/api/login')
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('password')
    if authenticate(email, senha):
        response = make_response('autenticado')
        session_id = session.sid if hasattr(session, 'sid') else None
        response.set_cookie('sessionId', session_id, httponly=True)
        return response
    return jsonify({'Mensagem': 'Erro de autenticação'}, 404)
@app.route('/api/feed', methods =['GET'] )
def feed():
    return json.dumps(getFeed())

if __name__=='__main__':
    app.run(debug=True)