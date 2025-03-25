from flask import Flask, render_template, request, redirect

from model.comments_controller import Comment
from model.users_controller import User

app = Flask(__name__)

# Página de login / cadastro

@app.route('/login')
def login_page():

    return render_template('login.html')

# Rota para Login
    
@app.route('/post/login', methods=['POST'])
def post_login_user():

    login = request.form.get('input-login')
    password = request.form.get('input-password')

    if (User.exists(login, password)):

        # Redirecionando de volta

        return 'Oi'
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'

# Página para cadastrar os comentários

@app.route('/')
def main_page():

    comentarios = Comment.get_comentarios()

    return render_template('formulario.html', comentarios=comentarios)

# Rota que receberá o formulário com o comentário

@app.route('/post/comentarios', methods=['POST'])
def post_comentarios():

    # Exportando as informações do formulário

    user = request.form.get('input-user')
    message = request.form.get('input-message')

    if (Comment.create(user, message)):

        # Redirecionando de volta

        Comment.get_comentarios()

        return redirect('/')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'
    
# Rota para apagar comentários
    
@app.route('/post/delete/<id>', methods=['POST'])
def post_delete_comentarios(id):

    if (Comment.delete(id)):

        # Redirecionando de volta

        return redirect('/')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'
    
# Rota para like nos comentários
    
@app.route('/post/like/<id>', methods=['POST'])
def post_like_comentarios(id):

    if (Comment.add_like(id)):

        # Redirecionando de volta

        return redirect('/')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'
    
# Rota para dislike nos comentários
    
@app.route('/post/dislike/<id>', methods=['POST'])
def post_dislike_comentarios(id):

    if (Comment.remove_like(id)):

        # Redirecionando de volta

        return redirect('/')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'
 
app.run(debug=True, host='0.0.0.0', port=8080)