
import bcrypt #este é o modulo que criptografa a senha
import sqlite3 #esta é um modulo que simula um banco de dados, só que banco de dados de arquivo
from flask import Flask, request, render_template #render template renderiza uma página html
class SaveUser:
    app = Flask(__name__, template_folder='template') #pega a pasta que está os dois arquivos html
    def __init__():
        try:
            conexao = sqlite3.connect('banco.db')
            cursor = conexao.cursor()
            cursor.execute('''
CREATE TABLE IF NOT EXISTS salvar_user(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        senha VARCHAR(255)
)
''')
            conexao.commit()
            cursor.close()
            conexao.close()
            print('Tabela criada com sucesso !')
        except sqlite3.Error as e:
            print(e)
    @app.route('/salvar', methods=['POST', 'GET'])
    def salvar():
        if request.method=='POST':
            nome = request.form.get('nome')
            senha = request.form.get('senha')
            senha_byte = senha.encode('utf-8')
            salt= bcrypt.gensalt()
            senha_cript = bcrypt.hashpw(senha_byte, salt)
            try:
                conexao = sqlite3.connect('banco.db')
                cursor = conexao.cursor()
                cursor.execute('''INSERT INTO salvar_user(nome,senha) VALUES (?,?)''', (nome, senha_cript))
                
                conexao.commit()
                print('Uusário (a) salvo (a) com sucesso !')
                cursor.execute('SELECT * FROM salvar_user')
                for user in cursor.fetchall():
                    print(user)
                cursor.close()
                conexao.close()
            except sqlite3.Error as e:
                print(e)
            return f'Seja bem-vindo (a) {nome}'
        return render_template('registro.html')



    @app.route('/check', methods=['POST', 'GET'])
    def check():
        if request.method=='POST':
            nome = request.form.get('nome')
            senhaproc = request.form.get('senha')
            senha_byte = senhaproc.encode('utf-8')
            try:
                conexao = sqlite3.connect('banco.db')
                cursor = conexao.cursor()
                cursor.execute('''SELECT nome, senha FROM salvar_user WHERE nome = ?''', (nome,))
                dados = cursor.fetchone()#retorna uma tupla 
                if dados:
                    nome, senha = dados #desempacotando uma tupla
                    if bcrypt.checkpw(senha_byte, senha): #descodifica a senha e compara se as duas são correspondentes
                
                        return 'Usuário encontrado !'
                    else:
                        return render_template('login.html', codicao = 'Senha incorreta !')#este parametro é do login.html
                else:
                    return render_template('login.html', codicao = 'Usuário não encontrado')
                        

            except sqlite3.Error as e:
                print(e)

            finally:
                cursor.close()
                conexao.close()
        return render_template('login.html')
    app.run(debug=True)

SaveUser()
