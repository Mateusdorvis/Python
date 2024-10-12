import turtle

#fazendo uma  representação de um carbono
tartaruga = turtle.Turtle()
tartaruga2  = turtle.Turtle()
for _ in range(8):
    tartaruga.forward(100)
    tartaruga.left(90)
    tartaruga.right(30)
    tartaruga2.forward(100)
   
    tartaruga2.right(90)
    tartaruga2.left(30)

turtle.done()