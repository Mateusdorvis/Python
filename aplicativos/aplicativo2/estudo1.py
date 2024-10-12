import tkinter as tk

class MeuApp:
    def __init__(self, root : tk.Tk):
        self.root = root
        self.root.title('Aplicativo executavel com tkinter')
        self.label = tk.Label(self.root, text='Olá mundo !')
        self.label.pack()

if __name__=='__main__':
    root = tk.Tk()
    app = MeuApp(root)
    root.mainloop()