import tkinter as tk

class View:
    def __init__(self, root : tk.Tk) -> None:
        self.root = root
        self.root.title('Gerenciamento de usuários com tkinter')

        self.listbox = tk.Listbox(self.root, width=200)
        self.listbox.grid(row=0, column = 0)

        self.frame = tk.Frame(self.root, borderwidth=1, relief='flat')
        self.frame.grid(row=1, column=0)

        self.scrollbar_list = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar_list.grid(row=0, column=1, sticky=tk.NS)
        self.listbox.config(yscrollcommand=self.scrollbar_list.set)

        self.entrada_nome()
        self.entrada_senha()

    def entrada_nome(self):
        self.info1 = tk.Label(self.frame, text='Digite seu nome : ')
        self.info1.grid(row=1, column=0)

        self.nome_entrada = tk.Entry(self.frame)
        self.nome_entrada.grid(row=1, column=1)

        self.info2 = tk.Label(self.frame, text='Digite seu nome  para deletar: ')
        self.info2.grid(row=2, column=0)

        self.nome_del = tk.Entry(self.frame)
        self.nome_del.grid(row=2, column=1)


        self.info3 = tk.Label(self.frame, text='Digite seu nome  para antigo: ')
        self.info3.grid(row=3, column=0)

        self.nome_update = tk.Entry(self.frame)
        self.nome_update.grid(row=3, column=1)

        self.info3 = tk.Label(self.frame, text='Digite seu novo nome: ')
        self.info3.grid(row=3, column=2)

        self.nome_update = tk.Entry(self.frame)
        self.nome_update.grid(row=3, column=3)
    
    
    
    def entrada_senha(self):
        self.info4 = tk.Label(self.frame, text='Digite sua senha : ')
        self.info4.grid(row=1, column=2, padx=5, pady=5)

        self.senha_entrada = tk.Entry(self.frame)
        self.senha_entrada.grid(row=1, column=3, padx=5, pady=5)

        self.info5 = tk.Label(self.frame, text='Digite sua senha para confirmar a deletação : ')
        self.info5.grid(row=2, column=2, padx=5, pady=5)

        self.senha_del = tk.Entry(self.frame)
        self.senha_del.grid(row=2, column=3, padx=5, pady=5)

        self.info5 = tk.Label(self.frame, text='Digite sua senha para confirmar a atualização do nome : ')
        self.info5.grid(row=3, column=4, padx=5, pady=5)

        self.senha_confi = tk.Entry(self.frame)
        self.senha_confi.grid(row=3, column=5)

        self.button_enviar = tk.Button(self.frame, text='Enviar')
        self.button_enviar.grid(row=2, column=0)
        
        self.button_del = tk.Button(self.frame, text='Deletar')
        self.button_del.grid(row=5, column=0)

        self.button_upd_nome = tk.Button(self.frame, text='Atualizar nome')
        self.button_upd_nome.grid(row=9, column=0)

        
        self.button_upd_senha = tk.Button(self.frame, text='Atualizar senha')
        self.button_upd_senha.grid(row=9, column=0)
    
    


    def get_senha(self, senha_entrada : tk.Entry):
        return senha_entrada.get()
    
    def get_nome(self, nome_entrada : tk.Entry):
        return nome_entrada.get()
    
    def inserir_usuario_listbox(self, nome, senha):
            return self.listbox.insert(tk.END, f'Nome do usuário : {nome}  |  Senha : {senha}')


View(tk.Tk())
tk.mainloop()