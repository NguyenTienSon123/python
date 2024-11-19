from turtle import Turtle, Screen

window = Screen()
contro = Turtle()


def vecuaso():
    contro.begin_fill()
    contro.color("red", "red")
    contro.forward(50)
    contro.left(90)
    contro.forward(50)
    contro.left(90)
    contro.forward(50)
    contro.end_fill()


def vengoinha():
    contro.color("orange", "orange")
    contro.begin_fill()
    # ve nha
    contro.forward(400)
    contro.left(90)
    contro.forward(240)
    contro.left(90)
    contro.forward(400)
    contro.left(90)
    contro.forward(240)
    contro.end_fill()

    contro.penup()
    contro.left(90)
    contro.forward(240)
    contro.left(90)
    contro.pendown()
    # ve cua ra vao
    contro.begin_fill()
    contro.color("red", "red")
    contro.forward(140)
    contro.left(90)
    contro.forward(80)
    contro.left(90)
    contro.forward(140)
    contro.end_fill()

    contro.penup()
    contro.left(90)
    contro.forward(210)
    contro.left(90)
    contro.forward(150)
    contro.pendown()
    # ve cua so
    vecuaso()

    contro.penup()
    contro.right(90)
    contro.forward(230)
    contro.right(90)
    contro.pendown()

    vecuaso()

    contro.penup()
    contro.right(90)
    contro.forward(100)
    contro.right(90)
    contro.forward(90)
    contro.pendown()

    # ve mai nha
    contro.begin_fill()
    contro.color("brown", "brown")
    contro.right(90)
    contro.forward(510)
    contro.left(120)
    contro.forward(80)
    contro.left(60)
    contro.forward(400)
    contro.end_fill()

    contro.penup()
    contro.right(180)
    contro.forward(90)
    contro.pendown()

    contro.begin_fill()
    contro.color("brown", "brown")
    contro.left(90)
    contro.forward(100)
    contro.end_fill()


def vengoisao():
    contro.penup()
    contro.forward(35)
    contro.pendown()
    contro.color("yellow", "yellow")
    contro.begin_fill()
    contro.left(108)
    contro.forward(100)
    for i in range(4):
        contro.left(144)
        contro.forward(100)
    contro.left(180)
    contro.forward(60)
    for i in range(4):
        contro.right(72)
        contro.forward(23.5)
    contro.end_fill()


def velaco():
    contro.color("red", "red")
    contro.begin_fill()
    contro.forward(105)
    contro.left(90)
    contro.forward(140)
    contro.left(90)
    contro.forward(210)
    contro.left(90)
    contro.forward(140)
    contro.left(90)
    contro.forward(105)
    contro.end_fill()

    contro.penup()
    contro.left(90)
    contro.forward(20)
    contro.right(90)
    contro.pendown()

    contro.begin_fill()
    vengoisao()

    contro.end_fill()


velaco()
contro.penup()
contro.left(54)
contro.forward(400)
contro.left(90)
contro.pendown()
vengoinha()


contro.hideturtle()
window.mainloop()
