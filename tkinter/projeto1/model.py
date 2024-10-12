from tkinter import messagebox
import sqlite3 as sql
import bcrypt
class GerenciaUser:
    def __init__(self):
        try:
            self.conexao = sql.connect('meu_banco_tkinter.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios_tkinter(
        nome VARCHAR(255),
        senha VARCHAR(255),
        UNIQUE(nome, senha)
)
''')
            self.conexao.commit()
            print('Tabela criada com sucesso !')
        except sql.Error as e :
            print(f'Deu pau na hora de criar a tabela : {e}')
        finally:
            self.cursor.close()
            self.conexao.close()
    
    def salvar_usuario(self, nome : str, senha : str):
        senha_encode =  senha.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(senha_encode, salt)
        try:
            self.conexao = sql.connect('meu_banco_tkinter.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute('''SELECT * FROM  usuarios_tkinter WHERE nome = ? ''', (nome,))
            nome_user = self.cursor.fetchone()
            if nome_user:
                return messagebox.showwarning('Aviso', 'Você já está cadastrado !')
            self.cursor.execute('''INSERT INTO usuarios_tkinter(nome, senha) VALUES (?,?) ''', (nome, hash,))
            self.conexao.commit()
            print(f'Usuário (a)  {nome} inserido (a) com sucesso !')
            messagebox.showinfo('Boas - vindas ', 'Você foi inserido no banco de dados com sucesso !')


        except sql.Error as e :
            print(f'Deu pau : {e}')

    def show_users(self,func):
        try:
            self.conexao = sql.connect('meu_banco_tkinter.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute('SELECT * FROM usuarios_tkinter')
            for cada_usuario in self.cursor.fetchall():
                func(cada_usuario[0], cada_usuario[1])

        except sql.Error as e :
            print(f'Deu pau : {e}')


class DeleteUser:
     @staticmethod
     def delete_user(nome : str, senha : str):
        senha_encode =  senha.encode('utf-8')
        try:
            conexao = sql.connect('meu_banco_tkinter.db')
            cursor = conexao.cursor()
            cursor.execute('''SELECT nome, senha FROM  usuarios_tkinter WHERE nome = ? ''', (nome,))
            dados = cursor.fetchone()
            if dados:
                nome_banco, senha_banco = dados
                if bcrypt.checkpw(senha_encode, senha_banco):
                    cursor.execute('''DELETE FROM  usuarios_tkinter WHERE nome = ? ''', (nome,))
                    conexao.commit()
                    print(f'Usuário (a)  {nome} deletado !')
                    return messagebox.showinfo('Sucesso ', 'Seus dados foram apagaos com sucesso !')
                return messagebox.showwarning('Error','Senha ou nome incorreto !' )
            return messagebox.showwarning('Aviso', 'Nenhum usuário encontrado !')
        except sql.Error as e :
            print(f'Deu pau : {e}')

class UpdateUser:
    @staticmethod
    def atualizar_senha(nome : str, senha : str, senha_nova : str):
        senha_encode =  senha.encode('utf-8')
        senha_encode_nova = senha_nova.encode('utf-8')
        hash = bcrypt.hashpw(senha_encode_nova, bcrypt.gensalt())
        try:
            conexao = sql.connect('meu_banco_tkinter.db')
            cursor = conexao.cursor()
            cursor.execute('''SELECT nome, senha FROM  usuarios_tkinter WHERE nome = ? ''', (nome,))
            dados = cursor.fetchone()
            if dados:
                nome_banco, senha_banco = dados
                if bcrypt.checkpw(senha_encode, senha_banco):
                    cursor.execute('''UPDATE FROM  usuarios_tkinter SET senha = ?  WHERE nome = ? ''', (hash, nome,))
                    conexao.commit()
                    print(f'Senha atualizada !')
                    return messagebox.showinfo('Sucesso ', 'Sua senha foi alterada!')
                return messagebox.showwarning('Error','Senha ou nome incorreto !' )
            return messagebox.showwarning('Aviso', 'Nenhum usuário encontrado !')
        except sql.Error as e :
            print(f'Deu pau : {e}')
    
    @staticmethod
    def atualizar_nome(nome_antigo : str, senha : str, nome_novo : str):
        senha_encode =  senha.encode('utf-8')
        try:
            conexao = sql.connect('meu_banco_tkinter.db')
            cursor = conexao.cursor()
            cursor.execute('''SELECT nome, senha FROM  usuarios_tkinter WHERE nome = ? ''', (nome_antigo,))
            dados = cursor.fetchone()
            if dados:
                nome_banco, senha_banco = dados
                if bcrypt.checkpw(senha_encode, senha_banco):
                    cursor.execute('''UPDATE FROM  usuarios_tkinter SET nome = ?  WHERE nome = ? ''', (nome_novo, nome_antigo,))
                    conexao.commit()
                    print(f'Nome atualizado !')
                    return messagebox.showinfo('Sucesso ', 'Seu nome foi alterado com sucesso !')
                return messagebox.showwarning('Error','Senha ou nome incorreto !' )
            return messagebox.showwarning('Aviso', 'Nenhum usuário encontrado !')
        except sql.Error as e :
            print(f'Deu pau : {e}')