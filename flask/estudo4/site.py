from flask import Flask

app = Flask(__name__)

@app.route('/exibir_nome/<nome>') #a rota url será na função 'exibir_nome' com o paramêtro <nome>
def exibir_nome(nome):
    return f'''
<h1> Olá mundo </h1>
<p> Esta mensagem está sendo exibida diretamente da função "exibir_nome" com o parâmetro nome e sue valor é  {nome} !</p>
''' #vai exibir esta mensgame no site

app.run(debug=True) #vai odar no modo debug