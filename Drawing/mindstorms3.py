import turtle

def draw_diamond(some_turtle):
    some_turtle.forward(100)
    some_turtle.right(20)
    some_turtle.forward(100)
    some_turtle.right(160)
    some_turtle.forward(100)
    some_turtle.right(20)
    some_turtle.forward(100)

def draw_flower():
    window= turtle.Screen()
    window.bgcolor("white")
    # Create the turtle Brad - draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(100)
    for i in range(1,42):
        draw_diamond(brad)
        brad.right(2)
    brad.right(90)
    brad.forward(300)
    window.exitonclick()

draw_flower()
