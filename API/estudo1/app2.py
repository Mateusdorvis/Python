from flask import Flask, request, jsonify, render_template_string
import sqlite3 as sql
import bcrypt

app = Flask(__name__)


def create_table():
    try:
        with sql.connect('meu_banco.db') as conexao:
            cursor =  conexao.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS dados(
                           nome VARCHAR(255), 
                           senha VARCHAR(255)
                           )''')
            print('Tabela criada !')
            cursor.close()
            conexao.close()
    except sql.Error as e:
        print(e)
create_table()

@app.route('/adiciona_usuario', methods=['POST'])
def adiciona_usuario():
    try:
        nome = request.form['nome']
        senha = request.form['senha']
        senha_encode = senha.encode('utf-8')

        conexao = sql.connect('meu_banco.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM dados WHERE nome = ?', (nome,))
        name = cursor.fetchone()
        if name:
            return jsonify({'Error': 'Você já está cadastrado !'}), 404
        cursor.execute('INSERT INTO dados(nome, senha) VALUES (?,?) ', (nome, bcrypt.hashpw(senha_encode, bcrypt.gensalt())))
        conexao.commit()
        print('Usuário inserido (a) com sucesso no banco !')
        cursor.close()
        conexao.close()
        return jsonify({'Sucesso': 'Você foi inserido no banco de dados com sucesso !'}), 201
    except sql.Error as e:
        print(f'Deu pau : {e}')

@app.route('/formulario')
def formulario():
    site_form = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário (simulação de banco de dados com sqlite3)</title>
</head>
<style>
    *{
        font-family: Arial, Helvetica, sans-serif;
    }
    body{
        background-image: linear-gradient(to left, red, blue);
    }
  form>label, form>input{
    display: block;
    margin: 25px auto;
  }
  input[type="text"], input[type="password"]{
    border-radius: 20px;
    height: 25px;
    width: 300px;
  }
  input[type="submit"]{
    border-radius: 20px;
    height: 25px;
    width: 200px;
    background-color: rgb(0, 0, 0);
    color: white;
    text-transform: uppercase;
    transition: .5s ease-in-out;
  }
  input[type="submit"]:hover{
    background-color: blue;
    
  }
  div{
    width: 300px;
    height: 300px;
    background-color: white;
    border-radius: 20px;
    margin: auto;
    padding: 40px;
    top: 100px;
    position: relative;
   
  }
</style>
<body>
   <div>
    <h1>Registro</h1>
    <form action="/adiciona_usuario" method="post">
        <label for="nome">Digite seu nome</label>
        <input type="text" name="nome" id="nome" required>
        <label for="senha">Digite sua senha</label>
        <input type="password" name="senha" id="senha" required>
        <input type="submit" value="Enviar cadastro">
    </form>
   </div>
</body>
</html>
'''
    return render_template_string(site_form)

@app.route('/verificar_user_existente', methods=['POST'])
def verificar_user_existente():
    try:
        nome = request.form['nome']
        senha = request.form['senha']
        senha_encode = senha.encode('utf-8')

        conexao = sql.connect('meu_banco.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT nome, senha FROM dados WHERE nome = ?', (nome,))
        name = cursor.fetchone()
        if name:
            nome_user, senha_user = name
            if nome_user==nome and bcrypt.checkpw(senha_encode, senha_user):
                return jsonify({'Sucesso': 'Você foi encontrado !'})
            return jsonify({'Error': 'Senha ou nome incorreto !'}), 404
        return jsonify({'Aviso': 'Nenhum usuário encontrado com os dados fornecidos'}), 500
     
    except sql.Error as e:
        print(f'Deu pau : {e}')
@app.route('/check')
def check():
   return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login (simulação de banco de dados com sqlite3)</title>
</head>
<style>
    *{
        font-family: Arial, Helvetica, sans-serif;
    }
    body{
        background-image: linear-gradient(to left, red, blue);
    }
  form>label, form>input{
    display: block;
    margin: 25px auto;
  }
  input[type="text"], input[type="password"]{
    border-radius: 20px;
    height: 25px;
    width: 300px;
  }
  input[type="submit"]{
    border-radius: 20px;
    height: 25px;
    width: 200px;
    background-color: rgb(0, 0, 0);
    color: white;
    text-transform: uppercase;
    transition: .5s ease-in-out;
  }
  input[type="submit"]:hover{
    background-color: blue;
    
  }
  div{
    width: 300px;
    height: 300px;
    background-color: white;
    border-radius: 20px;
    margin: auto;
    padding: 40px;
    top: 100px;
    position: relative;
   
  }
</style>
<body>
   <div>
    <h1>Login</h1>
    <form action="/verificar_user_existente" method="post">
        <label for="nome">Digite seu nome</label>
        <input type="text" name="nome" id="nome" required>
        <label for="senha">Digite sua senha</label>
        <input type="password" name="senha" id="senha" required>
        <input type="submit" value="Enviar cadastro">
    </form>
   </div>
</body>
</html>
'''
@app.route('/show_users')
def show_users():
    try:
        conexao = sql.connect('meu_banco.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM dados ')
        dados = cursor.fetchall()
        if dados:
            dados_banco = ''.join(f'''
<tr>
    <td> {cada_dado[0]} </td>
    <td> {cada_dado[1]} </td>
</tr>
''' for cada_dado in dados)
            return '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    table, th, tr, td{
        border: 1px solid black;
        width: 500px;
        background : white;
    }
    body{
        background-color: #679db6;
        font-family: Arial, Helvetica, sans-serif;
    }
    
</style>
<body>
    <h1>Tabela de usuários cadastrados</h1>
    <table>
        <tr>
            <th>Nome</th>
            <th>Senha</th>
        </tr>
        %s
    </table>
</body>
</html>
                    '''%(dados_banco)
      
    except sql.Error as e:
        print(f'Deu pau : {e}')

app.run(debug=True)

    