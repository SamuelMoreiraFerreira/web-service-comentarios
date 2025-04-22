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

            cursor = conexao_db.cursor(dictionary=True)

            cursor.execute(f'SELECT {db_config["tb_users"]["fields"]["password"]}, {db_config["tb_users"]["fields"]["salt_password"]} FROM {db_config["tb_users"]["name"]} WHERE {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["login"]} = %s;', (login,))

            user = cursor.fetchone()

            print(user)

            print(sha256((password + user[db_config["tb_users"]["fields"]["salt_password"]]).encode()).hexdigest())

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            # Criptografa a senha inserida pelo usuário com o salt e verifica se corresponde à armazenada relacionada a conta

            if (not user or sha256((password + user[db_config["tb_users"]["fields"]["salt_password"]]).encode()).hexdigest() != user[db_config["tb_users"]["fields"]["password"]]):

                return False
            
            else:

                return True

        except:
            
            return False
        
    def register(username, login, password):

        try:

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