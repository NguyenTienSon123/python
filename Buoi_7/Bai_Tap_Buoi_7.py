from turtle import Turtle, Screen

window = Screen()
control = Turtle()


def cau1():
    control.color("orange", "red")
    control.begin_fill()
    for i in range(4):
        control.forward(100)
        control.left(90)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(20)
    control.right(90)
    control.forward(20)

    control.pendown()
    control.color("orange", "white")
    control.begin_fill()
    for i in range(4):
        control.forward(60)
        control.left(90)
    control.end_fill()


def cau2_1():
    control.color("red")
    control.begin_fill()
    for i in range(3):
        control.forward(100)
        control.left(120)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(45)
    control.right(90)
    control.forward(150)
    control.pendown()

    control.begin_fill()
    control.color("orange", "")
    control.left(90)
    control.forward(100)
    control.left(90)
    control.forward(190)
    control.left(90)
    control.forward(230)
    control.left(90)
    control.forward(190)
    control.left(90)
    control.forward(95)
    control.right(90)
    control.forward(29)
    control.right(90)
    control.forward(20)
    control.left(135)
    control.forward(50)
    control.left(90)
    control.forward(50)
    control.left(135)
    control.forward(20)
    control.right(90)
    control.forward(30)
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
    control.right(90)
    control.forward(caomt)
    control.right(90)
    control.forward(10)
    control.left(135)
    control.forward(20)
    control.left(90)
    control.forward(20)
    control.left(135)
    control.forward(10)
    control.right(90)
    control.forward(10)
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


def vexe():
    control.begin_fill()
    control.color("green", "green")
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


def cau2_2():
    vexe()

    control.left(180)
    control.forward(80)
    control.right(90)
    control.forward(70)
    control.left(90)

    ht()

    control.penup()
    control.left(90)
    control.forward(150)
    control.pendown()

    ht()

    control.penup()
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


def cau3():
    control.color("green", "purple")
    control.begin_fill()

    # Vẽ nửa trái của trái tim
    control.left(140)
    control.forward(113)

    # Vẽ cung tròn nửa trái
    control.circle(-57, 200)

    # Vẽ nửa phải của trái tim
    control.left(120)

    # Vẽ cung tròn nửa phải
    control.circle(-57, 200)

    # Vẽ đường thẳng xuống
    control.forward(113)

    control.end_fill()

    control.penup()
    control.goto(100, 0)
    control.pendown()
    control.left(140)
    control.color("green", "green")
    control.begin_fill()

    # Vẽ nửa trái của trái tim
    control.left(140)
    control.forward(113)

    # Vẽ cung tròn nửa trái
    control.circle(-57, 200)

    # Vẽ nửa phải của trái tim
    control.left(120)

    # Vẽ cung tròn nửa phải
    control.circle(-57, 200)

    # Vẽ đường thẳng xuống
    control.forward(113)

    control.end_fill()


def cau4_1():
    control.color("red")
    control.begin_fill()
    for i in range(4):
        control.forward(100)
        control.left(90)
        control.forward(50)
        control.left(90)
        control.forward(100)
        control.right(90)
    control.end_fill()


def cau4_2():
    control.color("green", "green")
    control.begin_fill()
    control.forward(120)
    control.right(90)
    control.forward(30)
    control.right(90)
    control.forward(120)
    control.right(90)
    control.forward(30)
    control.end_fill()

    control.penup()
    control.right(90)
    control.forward(80)
    control.left(90)
    control.forward(30)
    control.pendown()

    control.color("green", "green")
    control.begin_fill()
    control.circle(20)
    control.end_fill()

    control.penup()
    control.right(180)
    control.forward(90)
    control.left(180)
    control.pendown()

    control.color("green", "green")
    control.begin_fill()
    control.circle(20)
    control.end_fill()


def dauNhan():
    control.left(45)
    cau4_1()


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

    control.penup()
    control.right(180)
    control.forward(90)
    control.pendown()

    control.begin_fill()
    control.color("brown", "brown")
    control.left(90)
    control.forward(100)
    control.end_fill()


def vengoisao():
    control.penup()
    control.forward(35)
    control.pendown()

    control.color("yellow", "yellow")
    control.begin_fill()
    control.left(108)
    control.forward(100)
    for i in range(4):
        control.left(144)
        control.forward(100)
    control.left(180)
    control.forward(60)
    for i in range(4):
        control.right(72)
        control.forward(23.5)
    control.end_fill()


def velaco():
    control.color("red", "red")
    control.begin_fill()
    control.forward(105)
    control.left(90)
    control.forward(140)
    control.left(90)
    control.forward(210)
    control.left(90)
    control.forward(140)
    control.left(90)
    control.forward(105)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(20)
    control.right(90)
    control.pendown()

    control.begin_fill()
    vengoisao()
    control.end_fill()


def cau5():
    velaco()
    control.penup()
    control.left(54)
    control.forward(400)
    control.left(90)
    control.pendown()
    vengoinha()


def vongLapHinhTron():
    control.begin_fill()
    i = 0
    while i < 8:
        control.circle(30)
        control.left(45)
        i += 1
    control.end_fill()


def hinhBinhHanh():
    control.color("black", "black")
    control.begin_fill()
    control.forward(100)
    control.left(45)
    control.forward(70)
    control.left(135)
    control.forward(100)
    control.left(45)
    control.forward(70)
    control.end_fill()


def hinhThang():
    control.color("black", "black")
    control.begin_fill()
    control.forward(130)
    control.left(135)
    control.forward(70)
    control.left(45)
    control.forward(60)
    control.left(60)
    control.forward(58)
    control.end_fill()


def hinhTamGiac():
    control.color("magenta")
    control.begin_fill()
    for i in range(3):
        control.forward(100)
        control.left(120)
    control.end_fill()


def hinhChop():
    control.color("magenta")
    control.begin_fill()
    control.right(100)
    hinhTamGiac()
    control.right(30)
    control.forward(100)
    control.left(105)
    control.forward(50)
    control.end_fill()


def veMatCuoi():
    control.begin_fill()
    control.color("yellow")
    control.circle(70, 360)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(30)
    control.left(90)
    control.forward(30)
    control.left(140)
    control.pendown()

    control.begin_fill()
    control.color("black", "")
    control.circle(50, 100)
    control.end_fill()

    control.penup()
    control.left(30)
    control.forward(50)
    control.pendown()

    control.begin_fill()
    control.color("black", "black")
    control.circle(15, 360)
    control.end_fill()

    control.penup()
    control.left(70)
    control.forward(50)
    control.pendown()

    control.begin_fill()
    control.color("black", "black")
    control.circle(15, 360)
    control.end_fill()


def mayTinh():
    control.color("orange", "red")
    control.begin_fill()
    control.forward(300)
    control.left(90)
    control.forward(200)
    control.left(90)
    control.forward(300)
    control.left(90)
    control.forward(200)
    control.left(90)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(20)
    control.right(90)
    control.forward(20)
    control.pendown()

    control.color("orange", "white")
    control.begin_fill()
    control.forward(260)
    control.left(90)
    control.forward(160)
    control.left(90)
    control.forward(260)
    control.left(90)
    control.forward(160)
    control.end_fill()

    control.penup()
    control.left(90)
    control.forward(90)
    control.right(90)
    control.forward(20)
    control.pendown()

    control.color("orange", "red")
    control.begin_fill()
    control.forward(25)
    control.left(90)
    control.forward(90)
    control.left(90)
    control.forward(25)
    control.end_fill()

    control.penup()
    control.forward(40)
    control.left(90)
    control.forward(20)
    control.right(180)
    control.pendown()

    veMatCuoi()


def binhHoa():
    control.begin_fill()
    control.color("red", "yellow")
    vongLapHinhTron()
    control.end_fill()

    control.penup()
    control.left(90)
    control.left(90)
    control.left(90)
    control.forward(60)
    control.pendown()

    control.begin_fill()
    control.color("black", "red")
    control.forward(50)
    control.right(90)
    control.forward(50)
    control.left(90)
    control.forward(90)
    control.left(90)
    control.forward(100)
    control.left(90)
    control.forward(90)
    control.left(90)
    control.forward(50)
    control.end_fill()

binhHoa()
control.hideturtle()
window.mainloop()
