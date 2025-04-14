from data.connection_controller import Connection
from hashlib import sha256
from flask import session

# DB Configuração JSON

import json

with open('db_config.json') as f:

    db_config = json.load(f)

class User:

    def exists(login, password):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute(f'SELECT * FROM {db_config["tb_users"]["name"]} WHERE BINARY {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["login"]} = %s;', (login,))

            salt_password = cursor.fetchone()[db_config["tb_users"]["fields"]["salt_password"]]

            password = sha256((password + salt_password).encode()).hexdigest()

            cursor.execute(f'SELECT * FROM {db_config["tb_users"]["name"]} WHERE BINARY {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["login"]} = %s AND BINARY {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["password"]} = %s;', (login, password))

            user = cursor.fetchone()

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            print(user)

            return True

        except:
            
            return False
        
    def register(username, login, password):

        try:

            # Criptogrando a senha em sha256

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute(f'INSERT INTO {db_config["tb_users"]["name"]} ({db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["username"]}, {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["login"]}, {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["password"]}) VALUES (%s, %s, %s);', (username, login, password))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False
        
    def create_session(login):
        
        session['login'] = login
        
    def logout():
        
        # Limpando os dados da sessão
        
        session.clear()