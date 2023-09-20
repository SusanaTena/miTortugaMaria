import turtle

miTortugaMaria = turtle.Turtle()

respuesta = input("¿Quieres un triángulo?")

if respuesta == "S" or "s":
    for _ in range (0,3):
        miTortugaMaria.forward (100)
        miTortugaMaria.left (120)
else:
    for _ in range(0, 3):
        miTortugaMaria.forward(100)
        miTortugaMaria.left(90)
