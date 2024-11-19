import random
from tkinter import *

from turtle import Turtle, Screen

cs = Screen()
control = Turtle()
control.speed(1000)

window = Tk()
window.geometry("1100x500")


def giaiThua():
    try:
        n = int(entry_n.get())
        gt = 1
        for i in range(n):
            gt *= (i + 1)
        entry_kq.delete(0, END)
        entry_kq.insert(0, str(gt))
        entry_n.delete(0, END)
    except ValueError:
        entry_n.delete(0, END)
        entry_n.insert(0, "Đâu vào không hợp lệ")


def cong():
    try:
        b = float(entry_a.get())
        a = float(entry_b.get())
        tong = a + b
        chuoi = str(a) + "+" + str(b) + "=" + str(tong)
        entry_kq.delete(0, END)
        entry_kq.insert(0, str(tong))
        entry_b.delete(0, END)
        entry_a.delete(0, END)
    except ValueError:
        entry_b.delete(0, END)
        entry_b.insert(0, "Đâu vào không hợp lệ")
        entry_a.delete(0, END)
        entry_a.insert(0, "Đâu vào không hợp lệ")


def tru():
    try:
        b = float(entry_b.get())
        a = float(entry_a.get())
        hieu = a - b
        chuoi = str(a) + "-" + str(b) + "=" + str(hieu)
        entry_kq.delete(0, END)
        entry_kq.insert(0, str(hieu))
        entry_b.delete(0, END)
        entry_a.delete(0, END)
    except ValueError:
        entry_b.delete(0, END)
        entry_b.insert(0, "Đâu vào không hợp lệ")
        entry_a.delete(0, END)
        entry_a.insert(0, "Đâu vào không hợp lệ")


def nhan():
    try:
        b = float(entry_b.get())
        a = float(entry_a.get())
        tich = a * b
        chuoi = str(a) + "x" + str(b) + "=" + str(tich)
        entry_kq.delete(0, END)
        entry_kq.insert(0, str(tich))
        entry_a.delete(0, END)
        entry_b.delete(0, END)
    except ValueError:
        entry_b.delete(0, END)
        entry_b.insert(0, "Đâu vào không hợp lệ")
        entry_a.delete(0, END)
        entry_a.insert(0, "Đâu vào không hợp lệ")


def chia():
    try:
        b = float(entry_b.get())
        a = float(entry_a.get())
        thuong = a / b
        chuoi = str(a) + ":" + str(b) + "=" + str(thuong)
        entry_kq.delete(0, END)
        entry_kq.insert(0, str(thuong))
        entry_b.delete(0, END)
        entry_a.delete(0, END)
    except ValueError:
        entry_b.delete(0, END)
        entry_b.insert(0, "Đâu vào không hợp lệ")
        entry_a.delete(0, END)
        entry_a.insert(0, "Đâu vào không hợp lệ")


def rda():
    entry_a.delete(0, END)
    a = random.randint(-1000, 1000)
    entry_a.insert(0, str(a))


def rdb():
    entry_b.delete(0, END)
    b = random.randint(-1000, 1000)
    entry_b.insert(0, str(b))


def giaibac1():
    try:
        b = float(entry_b2.get())
        a = float(entry_a2.get())
        if a == 0 and b == 0:
            entry_x.delete(0, END)
            entry_x.insert(0, "Phuong trinh vo so nghiem")
        else:
            if a != 0 and b == 0:
                entry_x.delete(0, END)
                entry_x.insert(0, "Phuong trinh vo nghiem")
            else:
                x = -b/a
                chuoi = str(x)
                entry_x.delete(0, END)
                entry_x.insert(0, chuoi)
                entry_b2.delete(0, END)
                entry_a2.delete(0, END)
    except ValueError:
        entry_b2.delete(0, END)
        entry_b2.insert(0, "Đâu vào không hợp lệ")
        entry_a2.delete(0, END)
        entry_a2.insert(0, "Đâu vào không hợp lệ")


def calculate_identities():
    try:
        a = float(entry_identities.get())
        b = float(entry_identities_b.get())
        result_1 = f"(a+b)^2 = {a**2 + 2*a*b + b**2}"
        result_2 = f"(a-b)^2 = {a**2 - 2*a*b + b**2}"
        result_3 = f"a^2 - b^2 = {(a+b)*(a-b)}"
        result_4 = f"(a+b)^3 = {a**3 + 3*a**2*b + 3*a*b**2 + b**3}"
        entry_result_identities.delete("1.0", END)
        entry_result_identities.insert("1.0", f"{result_1}\n{result_2}\n{result_3}\n{result_4}")
    except ValueError:
        entry_result_identities.delete("1.0", END)
        entry_result_identities.insert("1.0", "Lỗi")


def hinhTamGiac():
    control.penup()
    control.goto(100, 200)
    control.pendown()
    control.color("magenta")
    control.begin_fill()
    for i in range(3):
        control.forward(100)
        control.left(120)
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
    control.penup()
    control.goto(10, 50)
    control.pendown()
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


label_N = Label(text="Nhap vao n de tinh giai thua")
label_N.place(x=10, y=10, width=200, height=20)

entry_n = Entry()
entry_n.place(x=200, y=10, width=100, height=20)

button_GT = Button(text="Tinh n!", command=giaiThua)
button_GT.place(x=330, y=10, width=100, height=20)

button_A = Button(text="Click random a", command=rda)
button_A.place(x=30, y=40, width=100, height=20)

entry_a = Entry()
entry_a.place(x=200, y=40, width=100, height=20)

button_b = Button(text="Click random b", command=rdb)
button_b.place(x=30, y=70, width=100, height=20)

entry_b = Entry()
entry_b.place(x=200, y=70, width=100, height=20)

label_kq = Label(text="Ket qua")
label_kq.place(x=10, y=100, width=200, height=20)

entry_kq = Entry()
entry_kq.place(x=200, y=100, width=100, height=20)

button_cong = Button(text="+", command=cong)
button_cong.place(x=330, y=40, width=20, height=20)

button_tru = Button(text="-", command=tru)
button_tru. place(x=330, y=70, width=20, height=20)

button_nhan = Button(text="x", command=nhan)
button_nhan. place(x=360, y=40, width=20, height=20)

button_chia = Button(text=":",  command=chia)
button_chia. place(x=360, y=70, width=20, height=20)

label_1 = Label(text="Phuong trinh bac nhat")
label_1.place(x=10, y=130, width=200, height=20)

label_a2 = Label(text="Nhap vao a")
label_a2.place(x=10, y=160, width=200, height=20)

entry_a2 = Entry()
entry_a2.place(x=200, y=160, width=100, height=20)

label_b2 = Label(text="Nhap vao b")
label_b2.place(x=10, y=190, width=200, height=20)

entry_b2 = Entry()
entry_b2.place(x=200, y=190, width=100, height=20)

button_x = Button(text="X = ", command=giaibac1)
button_x.place(x=100, y=220, width=40, height=20)

entry_x = Entry()
entry_x.place(x=200, y=220, width=100, height=20)

label_2 = Label(text="Hang dang thuc")
label_2.place(x=10, y=250, width=200, height=20)

label_identities = Label(text="Nhập a và b")
label_identities.place(x=10, y=280, width=100, height=25)
entry_identities = Entry()
entry_identities.place(x=80, y=310, width=100, height=25)
entry_identities_b = Entry()
entry_identities_b.place(x=200, y=310, width=100, height=25)
button_identities = Button(text="Tính hằng đẳng thức", command=calculate_identities)
button_identities.place(x=340, y=310, width=150, height=25)
entry_result_identities = Text()
entry_result_identities.place(x=50, y=350, width=400, height=80)


button_tamgiac = Button(text="Tam giac", command=hinhTamGiac)
button_tamgiac.place(x=500, y=10, width=100, height=20)

button_maytinh = Button(text="May tinh", command=mayTinh)
button_maytinh.place(x=500, y=30, width=100, height=20)

control.hideturtle()
window.mainloop()
