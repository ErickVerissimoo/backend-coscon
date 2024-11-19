from flask import Flask
from models import db
app = Flask(__name__)

@app.route('/api')
def teste(): 
    return 'ola mundo'

if __name__=='__main__':
    app.run(debug=True)