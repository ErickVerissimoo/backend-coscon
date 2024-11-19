from flask import Flask, request, jsonify
from models.classes import *
from models.database import *
app = create_app()

@app.route('/api', methods=['POST'])
def cadastrar(): 
    data = request.json
    addUser(data.get('username'), data.get('email'),  data.get('password'))
    return jsonify({"Mensagem": "usuario cadastrado com sucesso!"})

if __name__=='__main__':
    
    app.run(debug=True)