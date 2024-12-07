# Instruções

para rodar a API, basta executar os seguintes comandos no terminal primeiro:

1. python3 (ou python se não for) -m venv .venv
2. pip install flask
3. pip install flask-SQLAlchemy
4. pip install voluptuous
5. pip install pymysql

depois altere a linha 9 do arquivo 'database.py' adicionando as credenciais do seu mysql e do seu banco, o SQLAlchemy se encarregará de criar as tabelas automaticamente ao 
iniciar a aplicação