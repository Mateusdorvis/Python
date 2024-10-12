import tkinter as tk 
from view import View
from tkinter import messagebox


class Controle:
    def __init__(self, root):
        self.view = View(root)
        #configurando o botao
        self.view.button.config(command=self.enviar)
    
    def enviar(self):
        peso = self.view.getPeso()
        altura = self.view.getAltura()
        if peso=='' and altura=='':
            messagebox.showwarning('Atenção', 'Por favor preencha os campos !')
        elif peso!='' and altura=='':
            messagebox.showwarning('Atenção', 'Por favor preencha o campo de altura !')
        elif peso=='' and altura!='':
            messagebox.showwarning('Atenção', 'Por favor preencha o campo de peso !')

        else:
            peso = float(peso.replace(',', '.'))
            altura = float(altura.replace(',', '.'))
            if altura >=10:
                altura/=100
            return  messagebox.showinfo('Cálculo ',self.calculo(peso, altura)) 


            
          
    
    def calculo(self, peso :float, altura :float):
    
        imc = peso/(altura**2)

        if imc<=18.5:
             return f'Você está abaixo do peso, pois seu  índice de massa corporal é  de {imc:.2f}. '
        
        elif imc>=18.5 and imc<=24.9:
            return f'Seu peso está normal, pois seu  índice de massa corporal é  de {imc:.2f}. '
        
        elif imc>=25.0 and imc<=29.9:
            return f'Você está no sobepeso, pois seu  índice de massa corporal é de {imc:.2f}. '
        
        elif imc>=30.0 and imc<=34.9:
            return f'Você está no obesidade grau 1, pois seu  índice de massa corporal é de {imc:.2f}.'
        
        elif imc>=35.0 and imc<=39.9:
            return f'Você está no obesidade grau 2, pois seu  índice de massa corporal é de {imc:.2f}.'
        
        elif imc>=40.0:
            return f'Você está no obesidade grau 3 (obesidade mórbida), pois índice de massa corporal é de {imc:.2f} '
       
        

root = tk.Tk()
app = Controle(root)
root.mainloop()