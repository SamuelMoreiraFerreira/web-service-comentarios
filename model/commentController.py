from data.connectionController import Connection
import datetime

class Comment:

    def create(user, message):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute("INSERT INTO tb_comentarios (nome, comentario, data_hora) VALUES (%s, %s, %s);", (user, message, datetime.datetime.now()))

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

            cursor.execute("DELETE FROM tb_comentarios WHERE tb_comentarios.id = %s;", (id))

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

            cursor.execute('SELECT nome, comentario, data_hora FROM tb_comentarios;')

            # fetchall -> Todos os campos retornados do comando

            comentarios_lista = cursor.fetchall()

            cursor.close()
            conexao_db.close()

            return comentarios_lista

        except:

            return []