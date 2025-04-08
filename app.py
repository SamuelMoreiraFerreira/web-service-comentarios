from flask import Flask, render_template, request, redirect

from model.comments_controller import Comment
from model.users_controller import User

app = Flask(__name__)

# Página de login / cadastro

@app.route('/')
def login_page():

    return render_template('login.html')

# Rota para Login
    
@app.route('/post/login', methods=['POST'])
def post_login_user():

    login = request.form.get('input-login')
    password = request.form.get('input-password')

    if User.exists(login, password):

        return redirect('/comments')
    
    else:

        return redirect('/')
    
# Rota para Cadastro
    
@app.route('/post/register', methods=['POST'])
def post_register_user():

    username = request.form.get('input-username')
    login = request.form.get('input-login')
    password = request.form.get('input-password')

    if User.register(username, login, password):

        return redirect('/comments')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'

# Página para cadastrar os comentários

@app.route('/comments')
def main_page():

    return render_template('formulario.html', 
        comentarios=Comment.get_all()
    )

# Rota que receberá o formulário com o comentário

@app.route('/post/comentarios', methods=['POST'])
def post_comentarios():

    # Exportando as informações do formulário

    user = request.form.get('input-user')
    message = request.form.get('input-message')

    if Comment.create(user, message):

        # Redirecionando de volta

        return redirect('/comments')
    
    else:

        return '<a href="/comments">Erro. Tente Novamente.</a>'
    
# Rota para apagar comentários
    
@app.route('/post/delete/<id>', methods=['POST'])
def post_delete_comentarios(id):

    if Comment.delete(id):

        return redirect('/comments')
    
    else:

        return '<a href="/comments">Erro. Tente Novamente.</a>'
    
# Rota para like nos comentários
    
@app.route('/post/like/<id>', methods=['POST'])
def post_like_comentarios(id):

    if Comment.add_like(id):

        return redirect('/comments')
    
    else:

        return '<a href="/comments">Erro. Tente Novamente.</a>'
    
# Rota para dislike nos comentários
    
@app.route('/post/dislike/<id>', methods=['POST'])
def post_dislike_comentarios(id):

    if Comment.remove_like(id):

        return redirect('/comments')
    
    else:

        return '<a href="/comments">Erro. Tente Novamente.</a>'
 
app.run(debug=True, host='0.0.0.0', port=8080)