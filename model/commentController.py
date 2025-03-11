from data.connectionController import Connection

class Comment:

    def create(user, message):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute("INSERT INTO tb_comentarios (user, message) VALUES (%s, %s);", (user, message))

            # Confirma a alteração

            conexao_db.commit()

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            return True

        except:

            return False
        
    def get_comentarios():

        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor(dictionary=True)

            cursor.execute('SELECT user, message, dt FROM tb_comentarios')

            comentarios_lista = cursor.fetchall()

            cursor.close()
            conexao_db.close()

            return comentarios_lista

        except:

            return []