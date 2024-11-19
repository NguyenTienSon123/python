from tkinter import *
from tkinter import messagebox
import sqlite3
window = Tk()
window.title("Login")
window.geometry("300x200")
with sqlite3.connect("taikhoan.db") as db:
    cursor = db.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS
# nguoidung(
# id integer PRIMARY KEY,
# idname text NOT NULL,
# password text NOT NULL);""")

# cursor.execute("""INSERT INTO
# nguoidung(id,idname,password)
# VALUES
# ("1", "son", "123456"),
# ("2", "le", "123456"),
# ("3", "thi", "123456"),
# ("4", "thi", "123456");""")
# db.commit()

# cursor.execute("""CREATE TABLE IF NOT EXISTS
# sanpham(
# idsm integer PRIMARY KEY,
# name text NOT NULL);""")
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS
# khachhang(
# idkh integer PRIMARY KEY,
# name text NOT NULL);""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS
# donhang(
# iddh integer PRIMARY KEY,
# idkh integer,
# idsm integer);""")


def dangnhap():
    idname = entry_idname.get()
    mk = entry_mk.get()
    cursor.execute("SELECT nguoidung.password FROM nguoidung WHERE idname like ?", (idname,))
    for i in cursor.fetchall():
        e = str(i)
        e = e.replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        if e == mk:
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công")
            window.destroy()
            quanlymuaban()
        else:
            messagebox.showinfo("Đăng nhập", "Đăng nhập không thành công")


label_idname = Label(text="ID Name")
label_idname.place(x=20, y=20, width=100, height=20)
entry_idname = Entry()
entry_idname.place(x=110, y=20, width=100, height=20)

label_mk = Label(text="Password")
label_mk.place(x=20, y=50, width=100, height=20)
entry_mk = Entry()
entry_mk.place(x=110, y=50, width=100, height=20)

button_Login = Button(text="Login", command=dangnhap)
button_Login.place(x=100, y=100, width=100, height=20)


def quanlymuaban():
    window_quanlymuaban = Tk()
    window_quanlymuaban.title("Quan ly mua ban")
    window_quanlymuaban.geometry("350x300")

    button_sanpham = Button(window_quanlymuaban, text="San Pham", command=quanLySanPham)
    button_sanpham.place(x=10, y=10, width=100, height=20)

    button_khachhang = Button(window_quanlymuaban, text="KhachHang", command=quanLyKhachHang)
    button_khachhang.place(x=10, y=30, width=100, height=20)

    button_donhang = Button(window_quanlymuaban, text="DonHang", command=quanLyDonHang)
    button_donhang.place(x=10, y=50, width=100, height=20)


def quanLySanPham():
    def themSanPham():
        idsp = entry_idsp.get()
        tensp = entry_tensp.get()
        cursor.execute("""INSERT INTO sanpham (idsm,name)
        VALUES
        (?,?);""", (idsp, tensp))
        db.commit()
        list_SanPham.delete(0, END)
        cursor.execute("SELECT * FROM sanpham")
        for x in cursor.fetchall():
            list_SanPham.insert(0, x)
        entry_idsp.delete(0, END)
        entry_tensp.delete(0, END)

    def suasanpham():
        idsp = entry_idsp.get()
        tensp = entry_tensp.get()
        cursor.execute("""UPDATE sanpham SET name = ? WHERE idsm = ?;""", (tensp, idsp))
        db.commit()
        list_SanPham.delete(0, END)
        cursor.execute("SELECT * FROM sanpham")
        for x in cursor.fetchall():
            list_SanPham.insert(0, x)
        entry_idsp.delete(0, END)
        entry_tensp.delete(0, END)

    def xoasanpham():
        idsp = entry_idsp.get()
        cursor.execute("""DELETE FROM sanpham WHERE idsm = ?;""", (idsp, ))
        db.commit()
        list_SanPham.delete(0, END)
        cursor.execute("SELECT * FROM sanpham")
        for x in cursor.fetchall():
            list_SanPham.insert(0, x)
        entry_idsp.delete(0, END)
        entry_tensp.delete(0, END)

    def timKiem():
        idsp = entry_idsp.get()
        tensp = entry_tensp.get()
        if idsp != "" and tensp != "":
            list_SanPham.delete(0, END)
            cursor.execute("""SELECT * FROM sanpham WHERE idsm = ? AND name = ?;""", (idsp, tensp))
            for x in cursor.fetchall():
                list_SanPham.insert(0, x)
        else:
            if idsp == "" and tensp != "":
                list_SanPham.delete(0, END)
                cursor.execute("""SELECT * FROM sanpham WHERE name = ?;""", (tensp, ))
                for x in cursor.fetchall():
                    list_SanPham.insert(0, x)
            else:
                if idsp != "" and tensp == "":
                    list_SanPham.delete(0, END)
                    cursor.execute("""SELECT * FROM sanpham WHERE idsm = ?;""", (idsp, ))
                    for x in cursor.fetchall():
                        list_SanPham.insert(0, x)
                else:
                    messagebox.showinfo("Message", "Ban chua nhap gi")
        entry_idsp.delete(0, END)
        entry_tensp.delete(0, END)

    window_quanLySanPham = Tk()
    window_quanLySanPham.title("Quan ly san pham")
    window_quanLySanPham.geometry("350x300")

    label_tensp = Label(window_quanLySanPham, text="Ten San Pham")
    label_tensp.place(x=20, y=20, width=100, height=20)

    label_idsp= Label(window_quanLySanPham, text=" Ma san pham")
    label_idsp.place(x=20, y=50, width=100, height=20)

    entry_tensp = Entry(window_quanLySanPham)
    entry_tensp.place(x=110, y=20, width=100, height=20)

    entry_idsp = Entry(window_quanLySanPham)
    entry_idsp.place(x=110, y=50, width=100, height=20)

    button_them = Button(window_quanLySanPham, text="Them", command=themSanPham)
    button_them.place(x=100, y=100, width=30, height=20)

    button_sua = Button(window_quanLySanPham, text="Sua", command=suasanpham)
    button_sua.place(x=140, y=100, width=30, height=20)

    button_xoa = Button(window_quanLySanPham, text="Xoa", command=xoasanpham)
    button_xoa.place(x=180, y=100, width=30, height=20)

    button_TimKiem = Button(window_quanLySanPham, text="Tim Kiem", command=timKiem)
    button_TimKiem.place(x=240, y=100, width=50, height=20)

    list_SanPham = Listbox(window_quanLySanPham)
    list_SanPham.place(x=100, y=150, width=200, height=100)

    cursor.execute("SELECT * FROM sanpham")
    for x in cursor.fetchall():
        list_SanPham.insert(0, x)


def quanLyKhachHang():
    def themKhachHang():
        idkh = entry_idkh.get()
        tenkh = entry_tenkh.get()
        cursor.execute("""INSERT INTO khachhang (idkh,name)
        VALUES
        (?,?);""", (idkh, tenkh))
        db.commit()
        list_KhachHang.delete(0, END)
        cursor.execute("SELECT * FROM khachhang")
        for x in cursor.fetchall():
            list_KhachHang.insert(0, x)
        entry_idkh.delete(0, END)
        entry_tenkh.delete(0, END)

    def suaKhachHang():
        idkh = entry_idkh.get()
        tenkh = entry_tenkh.get()
        cursor.execute("""UPDATE khachhang SET name = ? WHERE idkh = ?;""", (tenkh, idkh))
        db.commit()
        list_KhachHang.delete(0, END)
        cursor.execute("SELECT * FROM khachhang")
        for x in cursor.fetchall():
            list_KhachHang.insert(0, x)
        entry_idkh.delete(0, END)
        entry_tenkh.delete(0, END)

    def xoaKhachHang():
        idkh = entry_idkh.get()
        cursor.execute("""DELETE FROM khachhang WHERE idkh = ?;""", (idkh, ))
        db.commit()
        list_KhachHang.delete(0, END)
        cursor.execute("SELECT * FROM khachhang")
        for x in cursor.fetchall():
            list_KhachHang.insert(0, x)
        entry_idkh.delete(0, END)
        entry_tenkh.delete(0, END)

    def timKiem():
        idkh = entry_idkh.get()
        tenkh = entry_tenkh.get()
        if idkh != "" and tenkh != "":
            list_KhachHang.delete(0, END)
            cursor.execute("""SELECT * FROM khachhang WHERE idkh = ? AND name = ?;""", (idkh, tenkh))
            for x in cursor.fetchall():
                list_KhachHang.insert(0, x)
        else:
            if idkh == "" and tenkh != "":
                list_KhachHang.delete(0, END)
                cursor.execute("""SELECT * FROM khachhang WHERE name = ?;""", (tenkh, ))
                for x in cursor.fetchall():
                    list_KhachHang.insert(0, x)
            else:
                if idkh != "" and tenkh == "":
                    list_KhachHang.delete(0, END)
                    cursor.execute("""SELECT * FROM khachhang WHERE idkh = ?;""", (idkh, ))
                    for x in cursor.fetchall():
                        list_KhachHang.insert(0, x)
                else:
                    messagebox.showinfo("Message", "Ban chua nhap gi")
        entry_idkh.delete(0, END)
        entry_tenkh.delete(0, END)


    window_quanLySanPham = Tk()
    window_quanLySanPham.title("Quan ly san pham")
    window_quanLySanPham.geometry("350x300")

    label_tenkh = Label(window_quanLySanPham, text="Ten San Pham")
    label_tenkh.place(x=20, y=20, width=100, height=20)

    label_idkh= Label(window_quanLySanPham, text=" Ma san pham")
    label_idkh.place(x=20, y=50, width=100, height=20)

    entry_tenkh = Entry(window_quanLySanPham)
    entry_tenkh.place(x=110, y=20, width=100, height=20)

    entry_idkh = Entry(window_quanLySanPham)
    entry_idkh.place(x=110, y=50, width=100, height=20)

    button_them = Button(window_quanLySanPham, text="Them", command=themKhachHang)
    button_them.place(x=100, y=100, width=30, height=20)

    button_sua = Button(window_quanLySanPham, text="Sua", command=suaKhachHang)
    button_sua.place(x=140, y=100, width=30, height=20)

    button_xoa = Button(window_quanLySanPham, text="Xoa", command=xoaKhachHang)
    button_xoa.place(x=180, y=100, width=30, height=20)

    button_TimKiem = Button(window_quanLySanPham, text="Tim Kiem", command=timKiem)
    button_TimKiem.place(x=240, y=100, width=50, height=20)

    list_KhachHang = Listbox(window_quanLySanPham)
    list_KhachHang.place(x=100, y=150, width=200, height=100)

    cursor.execute("SELECT * FROM khachhang")
    for x in cursor.fetchall():
        list_KhachHang.insert(0, x)


def quanLyDonHang():
    def them():
        iddh = entry_iddh.get()
        idkh = entry_idkh.get()
        idsp = entry_idsp.get()
        cursor.execute("""INSERT INTO donhang(iddh, idkh, idsm)
        VALUES
        (?,?,?);""", (iddh, idkh, idsp))
        db.commit()
        list_donhang.delete(0, END)
        cursor.execute("SELECT * FROM donhang")
        for x in cursor.fetchall():
            list_donhang.insert(0, x)
        entry_iddh.delete(0, END)
        entry_idkh.delete(0, END)
        entry_idsp.delete(0, END)

    def capNhat():
        iddh = entry_iddh.get()
        idkh = entry_idkh.get()
        idsp = entry_idsp.get()
        cursor.execute("""UPDATE donhang SET idkh = ? AND idsm = ? WHERE iddh = ?;""", (idkh, idsp, iddh))
        db.commit()
        list_donhang.delete(0, END)
        cursor.execute("SELECT * FROM donhang")
        for x in cursor.fetchall():
            list_donhang.insert(0, x)
        entry_iddh.delete(0, END)
        entry_idkh.delete(0, END)
        entry_idsp.delete(0, END)

    window_quanLyDonHang = Tk()
    window_quanLyDonHang.title("Quan ly khach hang")
    window_quanLyDonHang.geometry("350x300")

    label_iddh = Label(window_quanLyDonHang, text="Ma don hang")
    label_iddh.place(x=20, y=20, width=100, height=20)

    label_idkh = Label(window_quanLyDonHang, text=" Ma Khach hang")
    label_idkh.place(x=20, y=50, width=100, height=20)

    label_idsp = Label(window_quanLyDonHang, text=" Ma San Pham")
    label_idsp.place(x=20, y=80, width=100, height=20)

    entry_iddh = Entry(window_quanLyDonHang)
    entry_iddh.place(x=130, y=20, width=100, height=20)

    entry_idkh = Entry(window_quanLyDonHang)
    entry_idkh.place(x=130, y=50, width=100, height=20)

    entry_idsp = Entry(window_quanLyDonHang)
    entry_idsp.place(x=130, y=80, width=100, height=20)

    button_them = Button(window_quanLyDonHang, text="Them", command=them)
    button_them.place(x=100, y=100, width=30, height=20)

    button_sua = Button(window_quanLyDonHang, text="Cap nhat", command=capNhat)
    button_sua.place(x=140, y=100, width=60, height=20)

    list_donhang = Listbox(window_quanLyDonHang)
    list_donhang.place(x=100, y=150, width=200, height=100)

    cursor.execute("SELECT * FROM donhang")
    for x in cursor.fetchall():
        list_donhang.insert(0, x)


window.mainloop()
