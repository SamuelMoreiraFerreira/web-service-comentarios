from data.connectionController import Connection

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

            cursor.execute(f'SELECT * FROM {db_config["tb_users"]["name"]} WHERE {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["login"]} = %s AND BINARY {db_config["tb_users"]["name"]}.{db_config["tb_users"]["fields"]["password"]} = %s;', (login, password))

            user = cursor.fetch()

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            print(user)

            return True

        except:
            
            return False