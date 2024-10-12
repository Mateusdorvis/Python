from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
app = Flask(__name__, template_folder='template')
app.secret_key = 'Minha_chave_secreta' 
login_manager = LoginManager()
login_manager.init_app(app)
usuario_salvo = {
    'Usuário 1' : {'Nome': 'Mateus', 'Senha': 'oi'}
    } #simulação de um banco de dados
class Usuario(UserMixin):#esta classe herda a classe Usermixin para que assim seja feito o gerencimento do usuário completo
    def __init__(self, nome_usuario):
        self.id = nome_usuario
@login_manager.user_loader#a função carregar usuário irá servi como argumento do parâmetro callback, ou seja, estamos utilizando o conceito de decorador
def carregar_usuario(usuario_nome) :
    if usuario_nome in usuario_nome: #verifica se usuario salvo está dentro do dicio, se sim adicona este user na classe 
        return Usuario(usuario_nome)
    else:
        return None
@app.route('/fazer_login', methods=['POST', 'GET'])
def fazer_login():
    if request.method=='POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        for user in usuario_salvo.values():
            if user['Nome']==nome and user['Senha']==senha:
                user_login = Usuario(nome)
                login_user(user_login)
                return redirect(url_for('casa')) #retornará para a função e não para a página
        return 'Senha ou nome inválidos !'#else (senão) :  irá da mensagem de erro ao retornar
    return render_template('login.html')#renderiza a página login.html

@app.route('/casa')
@login_required #a função casa é argumento como um todo do parâmetro 'func' da função login_required
def casa():
    return f'Seja bem -vindo (a) {current_user.id}' #retorna com a msg de boas vindas do usuário com id dele
@app.route('/logsaida')
def logsaida():
    logout_user()
    return redirect(url_for('fazer_login')) #retornará para a função "fazer_login" e não para a página
app.run(debug=True)
@login_manager.user_loader#a função carregar usuário irá servi como argumento do parâmetro callback, ou seja, estamos utilizando o conceito de decorador
def carregar_usuario(usuario_nome) :
    if usuario_nome in usuario_nome: #verifica se usuario salvo está dentro do dicio, se sim adicona este user na classe 
        return Usuario(usuario_nome)
    else:
        return None
@app.route('/fazer_login', methods=['POST', 'GET'])
def fazer_login():
    if request.method=='POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        for user in usuario_salvo.values():
            if user['Nome']==nome and user['Senha']==senha:
                user_login = Usuario(nome)
                login_user(user_login)
                return redirect(url_for('casa')) #retornará para a função e não para a página
        return 'Senha ou nome inválidos !'#else (senão) :  irá da mensagem de erro ao retornar
    return render_template('login.html')#renderiza a página login.html

@app.route('/casa')
@login_required #a função casa é argumento como um todo do parâmetro 'func' da função login_required
def casa():
    return f'Seja bem -vindo (a) {current_user.id}' #retorna com a msg de boas vindas do usuário com id dele
@app.route('/logsaida')
def logsaida():
    logout_user()
    return redirect(url_for('fazer_login')) #retornará para a função "fazer_login" e não para a página
app.run(debug=True)