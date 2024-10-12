import sqlite3 as sql
import bcrypt
import os

class GerenciaUsuario:
    def __init__(self):
        #cores para a estilização do terminal
        self.VERMELHO = '\033[31m'
        self.RESET = '\033[0m'
        self.AZUL = '\033[34m'
        self.AMARELO = '\033[33m'
        self.VERDE = '\033[32m'

        
        #tentando a conexão com o banco de dados
        try:
            self.conexao = sql.connect('meu_banco.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute('''
CREATE TABLE IF NOT EXISTS dados_usuarios(
    nome VARCHAR(255),
    senha VARCHAR(255)
)
''')
            self.conexao.commit()
            print(F'{self.VERDE} Tabela criada {self.RESET}!')
            


        except sql.Error as e:
            print(F'{self.VERMELHO} Error : {e} {self.RESET}!')
        
        finally:
            self.cursor.close()
            self.conexao.close()
            
               
  

    def post(self, nome : str, senha : str):
        senha_codificada  = senha.encode('utf-8')
        salt = bcrypt.gensalt()
        senha_criptografada = bcrypt.hashpw(senha_codificada, salt)
        try:
            with sql.connect('meu_banco.db') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT nome FROM dados_usuarios WHERE nome = ?', (nome,))
                nome_existente = cursor.fetchone()
                if nome_existente:
                    print(F'{self.VERMELHO} Existe um usuário com este nome ! Por favor troque para outro {self.RESET}!')
                   
                    return False
                else:
                    cursor.execute('INSERT INTO dados_usuarios(nome, senha ) VALUES (?,?)', (nome, senha_criptografada,))
                    conexao.commit()
                    
                    print(F'{self.VERDE} Usuário (o) inserido (a) com sucesso no banco de dados !{self.RESET}')
                   
                    return True

             

        except sql.Error as e:
            print(F'{self.VERMELHO} Error ao inserir o usuário (a) : {e} {self.RESET}!')
        
        except sql.Connection as c:
            print(F'{self.VERMELHO} Erro de conexão : {c} {self.RESET}!')
    
 

    def get_user(self, nome: str, senha: str):
        senha_encode = senha.encode('utf-8')
        try:
                conexao = sql.connect('meu_banco.db')
                cursor = conexao.cursor()
                cursor.execute('SELECT nome, senha FROM dados_usuarios WHERE nome = ?', (nome,))
                dados_usuario = cursor.fetchone()
                if dados_usuario:
                    nome_banco, senha_banco = dados_usuario

                    if nome==nome_banco and bcrypt.checkpw(senha_encode, senha_banco):
                        print(F'{self.VERDE} Usuário encontrado ! {self.RESET}!')
                     

                        return True

                    else:
                        print(f'{'\033[31m'} Senha ou nome incorretos {'\033[0m'} !')
                        return False
                else:
                    print(f'{'\033[31m'} Não existe um usuário cadastrado no banco  com este nome : {nome} {'\033[0m'}')
                    return False

        except sql.Error as e:
            print(F'{self.VERMELHO} Error : {e} {self.RESET}!')

        except sql.Connection as c:
            print(F'{self.VERMELHO} Erro de conxeão ; {c} {self.RESET}!')
    
    def delete_conta(self, nome : str, senha : str):
        senha_encode = senha.encode('utf-8')
        try:
            with sql.connect('meu_banco.db') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT nome, senha FROM dados_usuarios WHERE nome = ?', (nome,))
                dados_usuario = cursor.fetchone()
                if dados_usuario:
                    nome_banco, senha_banco = dados_usuario
                    if nome==nome_banco and bcrypt.checkpw(senha_encode, senha_banco):
                        cursor.execute('DELETE FROM dados_usuarios WHERE nome = ?', (nome,))
                        conexao.commit()
                        print(F'{self.VERDE} Sua conta foi excluída com sucesso ! {self.RESET}!')
                      
                        return True
                 
                    print(F'{self.VERMELHO} Nome ou senha incorreto {self.RESET}!')
                    return False
                print(f'{'\033[31m'} Não existe um usuário cadastrado no banco  com este nome : {nome} {'\033[0m'}')
                return False
        except sql.Error as e:
            print(F'{self.VERMELHO} Error : {e} {self.RESET}!')
        except sql.Connection as c:
            print(F'{self.VERMELHO} Error : {c} {self.RESET}!')
    
    def update_user(self, nome : str , senha : str, dicio : dict):
        senha_encode = senha.encode('utf-8')
        try:
            with sql.connect('meu_banco.db') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT nome, senha FROM dados_usuarios WHERE nome = ?', (nome,))
                dados_usuario = cursor.fetchone()
                if dados_usuario:
                    nome_banco, senha_banco = dados_usuario
                    if nome==nome_banco and bcrypt.checkpw(senha_encode, senha_banco):
                        try :
                            pergunta = int(input('Digite 1 para mudar a senha e 2 para mudar o nome :'))
                            if pergunta == 1:
                                nome_novo = input('Digite seu novo nome :')

                                if nome_novo=='':
                                    print(F'{self.VERMELHO}  NÃO DEIXE VAZIO ESTE CAMPO  !{self.RESET}!')

                                else:
                                    cursor.execute('UPDATE dados_usuarios SET nome = ? WHERE nome = ?', (nome_novo, nome,))
                                    conexao.commit()

                                    if nome in dicio.values():
                                        del dicio['Nome']
                                        dicio['Nome'] = nome_novo

                                    print(F'{self.VERDE} NOME alterado com sucesso !{self.RESET}!')

                            elif pergunta == 2:
                                senha_nova = input('Digite sua nova senha :')
                                if senha_nova=='':
                                    print(F'{self.VERMELHO} Não deixe vazio !{self.RESET}!')
                                else:
                                    cursor.execute('UPDATE dados_usuarios SET senha = ? WHERE nome = ?', (senha_nova, nome,))
                                    conexao.commit()
                                    print(F'{self.VERDE}  SENHA atualizada com sucesso !{self.RESET}!')
                            else:
                                print(F'{self.VERMELHO} Esta opção não está disponível no momento {self.RESET}!')
                            
                            
                        except ValueError:
                            print(F'{self.VERMELHO} inválido  {self.RESET}!')

                        return True
                 
                    else:
                        print(F'{self.VERMELHO} Nome ou senha incorreto {self.RESET}!')
                        return False
                    
                print(f'{'\033[31m'} Não existe um usuário cadastrado no banco  com este nome : {nome} {'\033[0m'}')
                return False
            
        except sql.Error as e:
            print('Error  :', e)
   
    
  

    def show_informations(self, nome: str, senha : str):
        senha_encode = senha.encode('utf-8')
        try:
            with sql.connect('meu_banco.db') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT nome, senha FROM dados_usuarios WHERE nome = ?', (nome,))
                dados_usuario = cursor.fetchone()
                if dados_usuario:
                    nome_banco, senha_banco = dados_usuario
                    if nome==nome_banco and bcrypt.checkpw(senha_encode, senha_banco):
                        cursor.execute('SELECT * FROM  dados_usuarios WHERE nome = ?', (nome,))
                        for cada_dado in cursor.fetchall():
                            print(f'''
{self.AMARELO}
DADOS DO USUÁRIO (A) {nome}:
SENHA CRIPTOGRAFADA : {cada_dado[1]},
SENHA REAL : {senha}
{self.RESET}
''')
                        return True
                    print(F'{self.VERMELHO} Nome ou senha incorreto {self.RESET}!')
                    return False
                print(f'{'\033[31m'} Não existe um usuário cadastrado no banco  com este nome : {nome} {'\033[0m'}')
                return False
        except sql.Error as e:
            print(F'{self.VERMELHO} Error :{e} {self.RESET}!')
        except sql.Connection as c:
            print(F'{self.VERMELHO} Error :{c} {self.RESET}!')

    
