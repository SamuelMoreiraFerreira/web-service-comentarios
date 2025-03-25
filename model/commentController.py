from data.connectionController import Connection
import datetime

# Configuração JSON

import json

with open('config.json') as f:

    config = json.load(f)


class Comment:

    def create(user, message):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute(f'INSERT INTO {config["tb_comments"]["name"]} ({config["tb_comments"]["fields"]["user"]}, {config["tb_comments"]["fields"]["user"]}, {config["tb_comments"]["fields"]["dt"]}) VALUES (%s, %s, %s);', (user, message, datetime.datetime.now()))

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

            cursor.execute(f'DELETE FROM {config["tb_comments"]["name"]} WHERE {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["id"]} = %s;', (id,))

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

            cursor.execute(f'UPDATE {config["tb_comments"]["name"]} SET {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["likes"]} = {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["likes"]} + 1 WHERE {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["id"]} = %s;', (id,))

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

            cursor.execute(f'UPDATE {config["tb_comments"]["name"]} SET {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["likes"]} = {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["likes"]} - 1 WHERE {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["id"]} = %s;', (id,))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True

        except:
            
            return False
        
    def get_comentarios():

        try:

            conexao_db = Connection.create()

            # dictionary -> Usar o nome do campo ao invés do índice

            cursor = conexao_db.cursor(dictionary=True)

            cursor.execute(f'SELECT {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["id"]}, {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["user"]}, {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["message"]}, {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["dt"]}, {config["tb_comments"]["name"]}.{config["tb_comments"]["fields"]["likes"]} FROM {config["tb_comments"]["name"]};')

            # fetchall -> Todos os campos retornados do comando

            comentarios_lista = cursor.fetchall()

            cursor.close()
            conexao_db.close()

            return comentarios_lista

        except:

            return []