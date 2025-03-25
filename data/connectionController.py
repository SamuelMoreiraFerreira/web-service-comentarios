import mysql.connector

# DB Configuração JSON

import json

with open('db_config.json') as f:

    db_config = json.load(f)

class Connection:

    def create():

        return mysql.connector.connect( 

            host = db_config['host'], 
            port = db_config['port'], 
            user = db_config['user'], 
            password = db_config['password'], 
            database = db_config['database']

        )