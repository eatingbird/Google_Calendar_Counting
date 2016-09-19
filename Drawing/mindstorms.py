import turtle

def define_shape(name, cursor_shape, line_color, draw_speed):
    name.shape(cursor_shape)
    name.color(line_color)
    name.speed(draw_speed)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
        
    define_shape(brad, "circle", "yellow", 2)
    for e in range(0, 4):
        brad.forward(100)
        brad.right(90)

    define_shape(angie,"circle", "blue",1)
    angie.circle(100)

    define_shape(morea,"circle", "white", 2)
    for e in range(0,3):
        morea.right(45)
        morea.forward(50)

    window.exitonclick()

draw_shape()
