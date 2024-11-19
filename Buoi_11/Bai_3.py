from tkinter import *
window = Tk()
window.title("jf")
window.geometry("1000x700")

selecl_col = StringVar(window)
selecl_col.set("Sellect name:")
list_menu = OptionMenu(window,selecl_col, "red", "white", "yellow")


def clicked():
    chooseCololour = selecl_col.get()
    window.configure(bg=chooseCololour)


clickName = Button(text="click", command=clicked)
clickName.place(x=100, y=250, width=70, height=30)

list_menu.place(x=10, y=10, width=100, height=100)

window.mainloop()
