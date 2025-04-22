from data.connection_controller import Connection

# DB Configuração JSON

import json

with open('db_config.json') as f:

    db_config = json.load(f)

class Comment:

    def create(user, message):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute(f'INSERT INTO {db_config["tb_comments"]["name"]} ({db_config["tb_comments"]["fields"]["user"]}, {db_config["tb_comments"]["fields"]["message"]}) VALUES (%s, %s);', (user, message))

            # Confirma a alteração

            conexao_db.commit()

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False
        
    def delete(id):

        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute(f'DELETE FROM {db_config["tb_comments"]["name"]} WHERE {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["id"]} = %s;', (id,))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False
        
    def add_like(id):

        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute(f'UPDATE {db_config["tb_comments"]["name"]} SET {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} = {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} + 1 WHERE {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["id"]} = %s;', (id,))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False
        
    def remove_like(id):

        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute(f'UPDATE {db_config["tb_comments"]["name"]} SET {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} = {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} - 1 WHERE {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["id"]} = %s;', (id,))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False
        
    def get_all():

        try:

            conexao_db = Connection.create()

            # dictionary -> Usar o nome do campo ao invés do índice

            cursor = conexao_db.cursor(dictionary=True)

            cursor.execute(f'SELECT {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["id"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["user"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["message"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["dt"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} FROM {db_config["tb_comments"]["name"]} ORDER BY {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} DESC;')

            # fetchall -> Todos os campos retornados do comando

            comentarios_lista = cursor.fetchall()

            cursor.close()
            conexao_db.close()

            return comentarios_lista

        except:

            return []
        
    def get_last(user):

        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor(dictionary=True)

            cursor.execute(f'SELECT {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["id"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["user"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["message"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["dt"]}, {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["likes"]} FROM {db_config["tb_comments"]["name"]} WHERE {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["user"]} = %s ORDER BY {db_config["tb_comments"]["name"]}.{db_config["tb_comments"]["fields"]["id"]} DESC;', (user,))

            last_comment = cursor.fetchone()

            cursor.close()
            conexao_db.close()

            return last_comment

        except:

            return False