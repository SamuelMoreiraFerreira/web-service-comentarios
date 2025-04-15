from flask import Flask, render_template, request, redirect, session, jsonify

from model.comments_controller import Comment
from model.users_controller import User

app = Flask(__name__)

app.secret_key = 'AlexStocco'

# Página de login / cadastro

@app.route('/')
def login_page():

    return render_template('home_page.html', is_login=('login' in session))

# Página de comentários

@app.route('/comments')
def main_page():

    if ('login' in session):
        
        return render_template('comments_page.html', 
            comentarios=Comment.get_all()
        )
        
    else:
        
        return redirect('/')
    
# Página do Heisenberg...

@app.route('/heisenberg')
def heisenberg_page():
    
    return render_template('heisenberg_page.html')

@app.route('/api/get/messages')
def api_get_messages():

    messages = Comment.get_all()
    return jsonify(messages) 

@app.route('/api/get/lastmsg/<user>')
def api_get_last_message(user):

    message = Comment.get_last(user)

    print(message)

    return jsonify(message) 
    
#region Funcionalides - Usuários

# Rota para Login
    
@app.route('/post/login', methods=['POST'])
def post_login_user():

    login = request.form.get('input-login')
    password = request.form.get('input-password')

    if User.exists(login, password):

        session['login'] = login

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

# Página para Logout

@app.route('/logout')
def logout():
    
    User.logout()
    
    return redirect('/')

#endregion
    
#region Funcionalidades - Comentários

# Rota para criar comentários

@app.route('/post/comentarios', methods=['POST'])
def post_comentarios():

    # Exportando as informações do formulário

    message = request.form.get('input-message')

    if 'login' in session and Comment.create(session['login'], message):

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

#endregion

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=8080)