import turtle

miTortuga = turtle.Turtle()

strLados = input("¿Cuantos lados quieres?")

lados = int(strLados)

for _ in range(0, 360, 15):
    for _ in range(0, lados):
        miTortuga.forward(50)
        miTortuga.left(360/lados)
    miTortuga.left(15)
