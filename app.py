from flask import Flask, request, jsonify
from models.classes import *
from models.database import *
app = create_app()

@app.route('/api', methods=['POST'])
def cadastrar(): 
    data = request.json
    usee = User()
    usee.email = data.get('email')
    usee.username = data.get('username')
    usee.password = data.get('password')
    db.session.add(usee)
    db.session.commit()
    return jsonify({"Mensagem": "usuario cadastrado com sucesso!"})

if __name__=='__main__':
    
    app.run(debug=True)