from flask import Flask, render_template, request, redirect

from model.commentController import Comment

app = Flask(__name__)

comentarios = []

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
    
@app.route('/post/delete', methods=['POST'])
def post_delete_comentarios():

    return

app.run(debug=True, host='0.0.0.0', port=8080)