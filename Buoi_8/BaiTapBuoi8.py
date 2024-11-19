from turtle import Turtle, Screen

window = Screen()
control = Turtle()
control.speed(1000)

def vongLapHinhTron():
    control.begin_fill()
    i = 0
    while i < 8:
        control.circle(10)
        control.left(45)
        i += 1
    control.end_fill()


def cau1():
    control.begin_fill()
    control.color("red", "yellow")
    vongLapHinhTron()
    control.end_fill()

    control.penup()
    control.left(90)
    control.left(90)
    control.left(90)
    control.forward(20)
    control.pendown()

    control.begin_fill()
    control.color("black", "red")
    control.forward(20)
    control.right(90)
    control.forward(20)
    control.left(90)
    control.forward(40)
    control.left(90)
    control.forward(40)
    control.left(90)
    control.forward(40)
    control.left(90)
    control.forward(20)
    control.end_fill()


def vecuaso():
    control.begin_fill()
    control.color("red", "red")
    control.forward(50)
    control.left(90)
    control.forward(50)
    control.left(90)
    control.forward(50)
    control.end_fill()


def vengoinha():
    control.color("orange", "orange")
    control.begin_fill()
    # ve nha
    control.forward(400)
    control.left(90)
    control.forward(240)
    control.left(90)
    control.forward(400)
    control.left(90)
    control.forward(240)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(240)
    control.left(90)
    control.pendown()
    # ve cua ra vao
    control.begin_fill()
    control.color("red", "red")
    control.forward(140)
    control.left(90)
    control.forward(80)
    control.left(90)
    control.forward(140)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(210)
    control.left(90)
    control.forward(150)
    control.pendown()
    # ve cua so
    vecuaso()

    control.penup()
    control.right(90)
    control.forward(230)
    control.right(90)
    control.pendown()

    vecuaso()

    control.penup()
    control.right(90)
    control.forward(100)
    control.right(90)
    control.forward(90)
    control.pendown()

    # ve mai nha
    control.begin_fill()
    control.color("brown", "brown")
    control.right(90)
    control.forward(510)
    control.left(120)
    control.forward(80)
    control.left(60)
    control.forward(400)
    control.end_fill()


def ht():
    vai = 40
    day = 90
    cao = 40
    caomt = 10
    control.left(90)
    control.begin_fill()
    control.color("", "red")
    control.left(90)
    control.forward(vai)
    control.left(90)
    control.forward(cao)
    control.left(90)
    control.forward(day)
    control.left(90)
    control.forward(cao)
    control.left(90)
    control.forward(vai)
    control.end_fill()


def veBanh():
    control.begin_fill()
    control.color("blue", "blue")
    control.circle(30, 360)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(10)
    control.right(90)
    control.pendown()

    control.begin_fill()
    control.color("white", "white")
    control.circle(20, 360)
    control.end_fill()


def vekhungxe():
    control.begin_fill()
    control.color("black", "black")
    control.forward(450)
    control.left(90)
    control.forward(80)
    control.left(90)
    control.forward(90)
    control.right(90)
    control.forward(100)
    control.left(90)
    control.forward(360)
    control.end_fill()


def veXe():
    vekhungxe()

    control.left(180)
    control.forward(80)
    control.right(90)
    control.forward(70)
    control.left(90)

    ht()

    control.penup()
    control.left(180)
    control.forward(150)
    control.pendown()

    ht()

    control.penup()
    control.left(90)
    control.forward(150)
    control.pendown()

    veBanh()

    control.penup()
    control.begin_fill()
    control.right(90)
    control.forward(200)
    control.left(90)
    control.end_fill()
    control.pendown()

    veBanh()


def veDongSong():
    control.begin_fill()
    control.color("blue", "blue")
    control.right(50)
    control.forward(300)
    control.left(30)
    control.forward(100)
    control.right(60)
    control.forward(700)
    control.left(60)
    control.forward(150)
    control.left(120)
    control.forward(800)
    control.left(60)
    control.forward(100)
    control.right(30)
    control.forward(200)
    control.end_fill()


def vecau():
    control.begin_fill()
    control.color("orange", "orange")
    control.forward(120)
    control.left(90)
    control.forward(40)
    control.left(90)
    control.forward(120)
    control.left(90)
    control.forward(40)
    control.end_fill()


def may():
    control.penup()
    control.goto(500, 160)
    control.pendown()
    control.color("SkyBlue1", "SkyBlue1")
    control.setheading(90)
    control.begin_fill()
    control.circle(60, 180)
    control.end_fill()
    control.goto(440, 160)
    control.setheading(90)
    control.begin_fill()
    control.circle(80, 180)
    control.end_fill()


def vecay():
    control.begin_fill()
    control.color("green", "green")
    control.circle(70)
    control.end_fill()

    control.penup()
    control.left(180)
    control.forward(20)
    control.left(90)
    control.pendown()

    control.begin_fill()
    control.color("brown", "brown")
    control.forward(150)
    control.left(90)
    control.forward(40)
    control.left(90)
    control.forward(150)

    control.end_fill()

def bai2():
    may()
    control.penup()
    control.forward(350)
    control.left(90)
    control.pendown()
    vengoinha()
    control.penup()
    control.forward(500)
    control.left(90)
    control.forward(350)
    control.left(90)
    control.pendown()
    veXe()
    control.penup()
    control.goto(-900, 0)
    control.left(90)
    control.pendown()
    veDongSong()
    control.penup()
    control.goto(-300, 300)
    control.pendown()

    control.begin_fill()
    control.color("yellow", "yellow")
    control.circle(60)
    control.end_fill()

    control.penup()
    control.goto(-300, 10)
    control.right(130)
    control.pendown()

    vecay()

    control.penup()
    control.goto(-500, 10)
    control.right(90)
    control.pendown()

    vecay()


bai2()
control.hideturtle()
window.mainloop()