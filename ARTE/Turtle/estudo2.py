import turtle
import time
tartaruga = turtle.Turtle() #instância a classe
tartaruga.penup() #abaixa a caneta
tartaruga.goto(-100,0) #coloca a posição da caneta
tartaruga.pendown() #levanta a caneta
tela = turtle._Screen()
tela.title('Animação com turtle')
for letra in 'Eu amo python':
    tartaruga.write(letra, font=('Times new roman', 12 , 'normal'))
   
    tartaruga.forward(10) #distância cada caractere
    time.sleep(.2)

turtle.done()