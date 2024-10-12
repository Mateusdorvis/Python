import tkinter as tk

class View:
    def __init__(self, root : tk.Tk):
        self.root = root
        self.root.title('Calculadora de IMC (Índice de Massa Corporal)')
        

        self.label = tk.Label(self.root, text='Digite seu peso :')
        self.label.grid(row=0, column=0)

        self.entry_peso = tk.Entry(self.root)
        self.entry_peso.grid(row=0, column=1)

        self.label_altura = tk.Label(self.root, text='Digite sua altura :')
        self.label_altura.grid(row=1, column=0)

        self.entry_altura = tk.Entry(self.root)
        self.entry_altura.grid(row=1, column=1)

        self.button = tk.Button(self.root, text='Enviar')
        self.button.grid(row=2, column=0)
    
    def getPeso(self):
        return self.entry_peso.get()
    
    def getAltura(self):
        return self.entry_altura.get()


    
