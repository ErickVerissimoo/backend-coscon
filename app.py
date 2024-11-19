from flask import Flask, request, jsonify
from models.user import db
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def cadastrar(): 
    data = request.json
    nome = data.get('nome')
    return jsonify({"nome":nome, "mensagem":"oi pessoa"})

if __name__=='__main__':
    app.run(debug=True)