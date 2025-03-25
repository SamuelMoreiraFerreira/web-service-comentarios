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

            cursor.execute(f'SELECT * FROM {db_config['tb_comments']['name']} WHERE {db_config['tb_comments']['name']}.{db_config['tb_comments']['fields']['id']}', (user, message, datetime.datetime.now()))

            # Confirma a alteração

            conexao_db.commit()

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False