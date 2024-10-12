from flask import Flask

app = Flask(__name__)

@app.route('/comeco') #a rota url será na função 'comeco'
def comeco():
    return '''
<h1> Olá mundo </h1>
<p> Esta mensagem está sendo exibida diretamente da função "comeco" !</p>
''' #vai exibir esta mensgame no site

app.run(debug=True) #vai odar no modo debug