from flask import Flask, render_template, request, redirect

import mysql.connector

app = Flask(__name__)

comentarios = []

# Página para cadastrar os comentários

@app.route('/')
def main_page():

    return render_template('formulario.html', comentarios=)


# Rota que receberá o formulário com o comentário

insert_comentario = "INSERT INTO tb_comentarios (usuario, comentario) VALUES (%s, %s)"

@app.route('/post/comentarios', methods=['POST'])
def post_comentarios():

    # Exportando as informações do formulário

    usuario = request.form.get('usuario')
    comentario = request.form.get('comentario')

    # Adicionando à Database

    conexao_db = mysql.connector.connect( 

        host    ='localhost', 
        port=3306, 
        user='root', 
        password='root', 
        database='db_feedbacks'

    )

    # O cursor é responsável por manipular o banco de dados

    cursor = conexao_db.cursor()

    cursor.execute(insert_comentario, (usuario, comentario))

    # Confirma a alteração

    conexao_db.commit()

    # Fecha a conexão com o banco de dados e o cursor

    cursor.close()
    conexao_db.close()

    # Redirecionando de volta

    return redirect('/')

app.run(debug=True, host='0.0.0.0', port=8080)