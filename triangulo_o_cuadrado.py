import turtle

miTortugaMaria = turtle.Turtle()

respuesta = input("¿Quieres un triángulo?")

if respuesta == "S":
    for _ in range(0, 3):
        miTortugaMaria.forward(50)
        miTortugaMaria.left(120)

else:
    for _ in range(0, 4):
        miTortugaMaria.forward(50)
        miTortugaMaria.left(90)
