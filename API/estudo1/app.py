from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

#simula um banco de dados
dicionario_usuarios = [
    {'ID': 1, 'Nome': 'Mateus', 'Senha' : 'oi'},
    {'ID': 2, 'Nome': 'Ana', 'Senha' : '2024'},
]

@app.route('/dicionario_usuarios/', methods=['GET'])
def show_users():
    return jsonify(dicionario_usuarios) #retorna mostrando os dados

@app.route('/dicionario_usuarios/', methods=['POST'])
def add_user():
    nome = request.form['nome']    
    senha =  request.form['senha']
    x = len(dicionario_usuarios) + 1
    dicio = {'ID':  x, 'Nome': nome, 'Senha' :  senha}
    dicionario_usuarios.append(dicio)
    return jsonify({'Mensagem de Sucesso ! ': 'Você foi cadastrado com sucesso !'}), 201

@app.route('/dicionario_usuarios/<int:id>', methods=['GET'])
def mostrar_usuario(id):
    usuario_encontrado = next((cada_user for cada_user in dicionario_usuarios if cada_user['ID']==id), None) #este next é importante para que apareça os dados,  se fazer o loop normal, não irá aparecer os dados 
    if usuario_encontrado:
            return jsonify(usuario_encontrado)
    return jsonify({'Mensagem de erro ': 'Seu ID não encontrado !'}), 404

@app.route('/formulario')
def formulario():
    html_form = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário (simulação API)</title>
</head>
<style>
  form>label, form>input{
    display: block;
    margin: 5px;
  }
</style>
<body>
    <h1>Formulário</h1>
    <form action="/dicionario_usuarios/" method="post">
        <label for="nome">Digite seu nome</label>
        <input type="text" name="nome" id="nome">
        <label for="senha">Digite sua senha</label>
        <input type="password" name="senha" id="senha">
        <input type="submit" value="Enviar cadastro">
    </form>
</body>
</html>
    '''
    return render_template_string(html_form)#rendereiza a página de formulário HTML
app.run(debug=True)