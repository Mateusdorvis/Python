import turtle

tartaruga = turtle.Turtle()

tela = turtle.Screen()
tela.title('Meu primeiro desenho com turtle')
for _ in range(40):
    tartaruga.forward(10) #distância
    tartaruga.left(50) #ângulo do lado esquerdo
    tartaruga.right(70)#ângulo do lado esquerdo
#inicia o desenho
turtle.done()