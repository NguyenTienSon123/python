import os
from tkinter import *
window = Tk()
window.title("jf")
window.geometry("500x600")

anhCho = PhotoImage(file="cho.png")
anhMeo = PhotoImage(file="meo.png")
anhCa = PhotoImage(file="ca.png")
anhSon = PhotoImage(file="img.png")

window["bg"] = "orange"


def Cho():
    labe_Logo.config(image=anhCho)


def Meo():
    labe_Logo.config(image=anhMeo)


def Ca():
    labe_Logo.config(image=anhCa)


def Son():
    labe_Logo.config(image=anhSon)

sos = []


def add_number():
    value = entry.get()
    if value.isdigit():
        sos.append(value)
        entry.delete(0, END)
        listbox.insert(END, value)  # Thêm tên vào cuối danh sách hiển thị
    else:
        entry.delete(0, END)
        entry.insert(0, "Đâu vào không hợp lệ")


def clear_list():
    entry.delete(0, END)
    listbox.delete(0, END)


def thoat():
    exit()


label = Label(text="Enter a number")
label.place(x=5, y=10, width=100, height=20)

# Mục nhập cho đầu vào của người dùng
entry = Entry()
entry.place(x=120, y=10, width=160, height=20)

# Nút để thêm số
add_button = Button(window, text="Add list", command=add_number)
add_button.place(x=300, y=10, width=70, height=20)

total_label = Label(text="Lists")
total_label.place(x=5, y=40, width=100, height=20)

# Label to display total
listbox = Listbox()
listbox.place(x=120, y=40, width=160, height=140)

# Button to reset total
reset_button = Button(window, text="Clear list", command=clear_list)
reset_button.place(x=300, y=40, width=70, height=20)

exit_button = Button(window, text="Exit", command=thoat)
exit_button.place(x=300, y=100, width=70, height=20)


def print_list():
    # file = open("son.txt", "w")
    tmp_list = listbox.get(0, END)
    print("Danh sách các mục:")
    for item in tmp_list:
        file.write(item + "\n")
        print(item)
    file.close()


getlist_button = Button(window, text="Save List", command=print_list)
getlist_button.place(x=300, y=70, width=70, height=20)
#
# button_COnCho = Button(text="Open picture dog", command=Cho)
# button_COnCho.place(x=10, y=200, width=100, height=20)
#
# button_Conmeo = Button(text="Open picture cat", command=Meo)
# button_Conmeo.place(x=120, y=200, width=100, height=20)
#
# button_ConCa = Button(text="Open picture fish", command=Ca)
# button_ConCa.place(x=230, y=200, width=100, height=20)


def clicked():
    chooseCololour = selecl_img.get()
    if chooseCololour == "Cho":
        Cho()
    else:
        if chooseCololour == "Meo":
            Meo()
        else:
            if chooseCololour == "Ca":
                Ca()
            else:
                if chooseCololour == "Son":
                    Son()


clickName = Button(text="click", command=clicked)
clickName.place(x=130, y=230, width=70, height=30)

selecl_img = StringVar(window)
selecl_img.set("Sellect image:")
list_menu = OptionMenu(window, selecl_img, "Cho", "Meo", "Ca", "Son")
list_menu.place(x=10, y=230, width=120, height=30)

labe_Logo = Label(window, image="")
labe_Logo.place(x=10, y=280, width=300, height=300)

window.mainloop()
