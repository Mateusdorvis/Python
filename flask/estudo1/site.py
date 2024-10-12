from flask import Flask


app = Flask(__name__)

@app.route('/') #a rota será no servidor
def comeco():
    return 'Olá mundo, mensagem rodada diretamente do servidor  !' #vai exibir esta mensgame no site

app.run(debug=True) #vai odar no modo debug