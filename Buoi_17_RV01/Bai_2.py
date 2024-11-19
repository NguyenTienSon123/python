import tkinter as tk
import random
from tkinter import messagebox


def reset():
    global so_muc_tieu, so_luot_thu
    so_muc_tieu = random.randint(1, 100)
    so_luot_thu = 5
    entry_A.delete(0, tk.END)

def test():
    global so_luot_thu
    try:
        doan = int(entry_A.get())
    except ValueError:
        messagebox.showinfo("Kết Quả", f"Vui lòng nhập một số hợp lệ")
        return

    if doan < 1 or doan > 100:
        messagebox.showinfo("Kết Quả", f"Vui lòng nhập số từ 1 đến 100")
        return

    so_luot_thu -= 1
    if doan == so_muc_tieu:
        messagebox.showinfo("Kết Quả", "Chúc mừng! Bạn đã đoán đúng số!")
        reset()
    elif so_luot_thu > 0:
        messagebox.showinfo("Kết Quả", f"Bạn còn {so_luot_thu} lượt đoán")
    else:
        messagebox.showinfo("Kết Quả", f"Rất tiếc! Bạn đã hết lượt đoán. Số đúng là {so_muc_tieu}.")
        reset()


# Khởi tạo các biến toàn cục
so_muc_tieu = random.randint(1, 100)
so_luot_thu = 5

# Khởi tạo giao diện
root = tk.Tk()
root.title("Trò Chơi Đoán Số")
root.geometry("300x200")

label_A = tk.Label(root, text="Enter your number")
label_A.place(x=100, y=50, width=100, height=25)

entry_A = tk.Entry(root)
entry_A.place(x=100, y=90, width=100, height=25)

guess_button = tk.Button(root, text="Run", command=test)
guess_button.place(x=100, y=130, width=100, height=25)



root.mainloop()