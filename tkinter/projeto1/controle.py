from model import GerenciaUser, DeleteUser
from view import View
import tkinter as tk
from tkinter import messagebox

class Controle:
    def __init__(self, root):
        self.view = View(root)
        self.model =  GerenciaUser()
        self.config_button()
        self.model.show_users(self.view.inserir_usuario_listbox)

    def config_button(self):
        self.view.button_enviar.config(command=self.salvar)
        self.view.button_del.config(command=self.deletar)
    
    def salvar(self):
        self.view.listbox.delete(0, tk.END)
        nome =  self.view.get_nome(self.view.nome_entrada)
        senha = self.view.get_senha(self.view.senha_entrada)
        if nome=="" and senha=="":
            messagebox.showwarning('Aviso', 'Os campos estão vazios !')
        elif nome=="" or senha=="":
            messagebox.showwarning('Aviso', 'O campo nome ou senha está vazio !')
        else:
            self.model.salvar_usuario(nome, senha)
            self.view.senha_entrada.delete(0, tk.END)
            self.view.nome_entrada.delete(0, tk.END)
        self.model.show_users(self.view.inserir_usuario_listbox)
    
    def deletar(self):
        self.view.listbox.delete(0, tk.END)
        nome =  self.view.get_nome(self.view.nome_del)
        senha = self.view.get_senha(self.view.senha_del)
        if nome=="" and senha=="":
            messagebox.showwarning('Aviso', 'Os campos estão vazios !')
        elif nome=="" or senha=="":
            messagebox.showwarning('Aviso', 'O campo nome ou senha está vazio !')
        else:
            DeleteUser.delete_user(nome, senha)
            self.view.senha_entrada.delete(0, tk.END)
            self.view.nome_entrada.delete(0, tk.END)
        self.model.show_users(self.view.inserir_usuario_listbox)
