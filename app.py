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

@cookie_required('sessionId')
@app.route('/api/comentar', methods=['POST'])
def comentar():
    return jsonify({'mnsgm': 'Comentado'})
@app.route('/api/login')
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    usuario = findByEmailAndSenha(email, password)
   
    
    if authenticate(email, password) and usuario is not None:
        response = make_response('autenticado')
        session_id = session.sid if hasattr(session, 'sid') else None
        usuario.sessionId=session_id
        db.session.commit()
        response.set_cookie('sessionId', session_id, httponly=True)
        return response
    return jsonify({'Mensagem': 'Erro de autenticação'}, 404)
@app.route('/api/feed', methods =['GET'] )

def feed():
    return json.dumps(getFeed())
@app.route('/api/logout')
def logout():
    session.pop('sessionId', None)
    return jsonify({'msgm': 'Deslogado com sucesso'})
if __name__=='__main__':
    app.run(debug=True)