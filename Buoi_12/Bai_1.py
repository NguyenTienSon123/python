from tkinter import *


def solve_linear():
    try:
        a = float(entry_A.get())
        b = float(entry_B.get())
        if a == 0:
            if b == 0:
                result = "Phương trình có vô số nghiệm"
            else:
                result = "Phương trình vô nghiệm"
        else:
            result = f"x = {-b/a}"
        result_entry.delete(0, END)
        result_entry.insert(0, result)
    except ValueError:
        result_entry.delete(0, END)
        result_entry.insert(0, "Vui lòng nhập số hợp lệ")


def solve_quadratic():
    try:
        a = float(entry_A.get())
        b = float(entry_B.get())
        c = float(entry_C.get())
        if a == 0:
            if b == 0:
                result = "Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm"
            else:
                result = f"x = {-c/b}"
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                result = "Phương trình vô nghiệm"
            elif delta == 0:
                result = f"x = {-b/(2*a)}"
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                result = f"x1 = {x1}, x2 = {x2}"
        result_entry.delete(0, END)
        result_entry.insert(0, result)
    except ValueError:
        result_entry.delete(0, END)
        result_entry.insert(0, "Vui lòng nhập số hợp lệ")


window = Tk()
window.title("Bậc hai")
window.geometry("350x300")

label_A = Label(window, text="Nhập số A")
label_A.place(x=10, y=10, width=100, height=25)

entry_A = Entry(window)
entry_A.place(x=150, y=10, width=150, height=25)

label_B = Label(window, text="Nhập số B")
label_B.place(x=10, y=50, width=100, height=25)

entry_B = Entry(window)
entry_B.place(x=150, y=50, width=150, height=25)

label_C = Label(window, text="Nhập số C (bậc 2)")
label_C.place(x=10, y=90, width=100, height=25)

entry_C = Entry(window)
entry_C.place(x=150, y=90, width=150, height=25)

button_A = Button(window, text="Tính phương trình bậc 1", command=solve_linear)
button_A.place(x=50, y=130, width=200, height=25)

button_B = Button(window, text="Tính phương trình bậc 2", command=solve_quadratic)
button_B.place(x=50, y=170, width=200, height=25)

result_label = Label(window, text="Kết quả")
result_label.place(x=10, y=210, width=100, height=25)

result_entry = Entry(window)
result_entry.place(x=150, y=210, width=150, height=25)

window.mainloop()
