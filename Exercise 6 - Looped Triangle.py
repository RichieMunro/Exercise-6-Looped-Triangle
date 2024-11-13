import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Exercise 6 Triangle Loop")

richie = turtle.Turtle()
richie.color("blue")
richie.pensize(7) 

for f in [richie.forward(50), richie.left(120), richie.forward(50), richie.left(120), richie.forward(50), richie.left(120)]:
    triangle = richie
    print(triangle) 


wn.mainloop