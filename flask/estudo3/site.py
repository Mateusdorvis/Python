from flask import Flask, render_template
app = Flask(__name__, template_folder='template') #instancia a classe "Flask" e abre a pasta obrigatória template, para abrir a página html
@app.route('/comeco') #a rota será na função "comeco"
def comeco():
    name = 'Mateus'
    return render_template('index.html', nome=name)#retornará abrindo a url "index.html" da pasta obrigatoria "template"  e com o parâmetro "nome" da página "index.html" que recebe o valor "mateus" 
app.run(debug=True) #vai odar no modo debug