from tkinter import *
from tkinter import messagebox
import mysql.connector

window_quanlymuaban = Tk()
window_quanlymuaban.title("Library")
window_quanlymuaban.geometry("350x300")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="quanlythuvien"
)

mycursor = mydb.cursor()
# mycursor.execute("""CREATE DATABASE IF NOT EXISTS QuanLyThuVien""")
# mycursor.execute("""CREATE TABLE IF NOT EXISTS book (
# book_id INT(5) PRIMARY KEY,
# title VARCHAR(30),
# author VARCHAR(20),
# publication_year VARCHAR(4),
# available INT(5))""")

# mycursor.execute("""CREATE TABLE IF NOT EXISTS borrowings (
# borrowings_id INT PRIMARY KEY,
# book_id INT(5),
# user_name VARCHAR(20),
# borrow_date Date,
# return_date Date,
# foreign key (book_id) references book (book_id))""")


def thuVien():
    def themsach():
        ma = entry_idsach.get()
        ten = entry_tensach.get()
        tg = entry_tacgia.get()
        nam = entry_nam.get()
        sl = entry_tt.get()
        mycursor.execute("INSERT INTO book (book_id, title, author, publication_year, available) VALUES (%s, %s, %s, %s, %s)",
                         (ma, ten, tg, nam, sl))
        mydb.commit()
        list_sach.delete(0, END)
        mycursor.execute("SELECT * FROM book")
        for x in mycursor.fetchall():
            list_sach.insert(0, str(x))
        entry_idsach.delete(0, END)
        entry_tensach.delete(0, END)
        entry_tacgia.delete(0, END)
        entry_nam.delete(0, END)
        entry_tt.delete(0, END)

    def suasanpham():
        ma = entry_idsach.get()
        ten = entry_tensach.get()
        tg = entry_tacgia.get()
        nam = entry_nam.get()
        sl = entry_tt.get()
        mycursor.execute("UPDATE book SET title=%s, author=%s, publication_year=%s, available=%s WHERE book_id=%s",
                         (ten, tg, nam, sl, ma))
        mydb.commit()
        list_sach.delete(0, END)
        mycursor.execute("SELECT * FROM book")
        for x in mycursor.fetchall():
            list_sach.insert(0, str(x))
        entry_idsach.delete(0, END)
        entry_tensach.delete(0, END)
        entry_tacgia.delete(0, END)
        entry_nam.delete(0, END)
        entry_tt.delete(0, END)

    def xoasanpham():
        id = entry_idsach.get()
        mycursor.execute("DELETE FROM book WHERE book_id=%s", (id,))
        mydb.commit()
        list_sach.delete(0, END)
        mycursor.execute("SELECT * FROM book")
        for x in mycursor.fetchall():
            list_sach.insert(0, str(x))
        entry_idsach.delete(0, END)
        entry_tensach.delete(0, END)
        entry_tacgia.delete(0, END)
        entry_nam.delete(0, END)
        entry_tt.delete(0, END)

    def timKiem():
        search_name = entry_tensach.get()
        mycursor.execute("SELECT * FROM book WHERE title LIKE %s", (search_name,))
        books = mycursor.fetchall()
        list_sach.delete(0, tk.END)
        for book in books:
            list_sach.insert(tk.END, str(book))
        entry_idsach.delete(0, END)
        entry_tensach.delete(0, END)
        entry_tacgia.delete(0, END)
        entry_nam.delete(0, END)
        entry_tt.delete(0, END)

    window_quanLySanPham = Tk()
    window_quanLySanPham.title("Quan ly sach")
    window_quanLySanPham.geometry("350x500")

    label_idsach = Label(window_quanLySanPham, text=" Ma")
    label_idsach.place(x=20, y=20, width=100, height=20)

    label_tensach = Label(window_quanLySanPham, text="Ten")
    label_tensach.place(x=20, y=50, width=100, height=20)

    label_tacgia = Label(window_quanLySanPham, text="Tac Gia")
    label_tacgia.place(x=20, y=80, width=100, height=20)

    label_nam = Label(window_quanLySanPham, text="Nam")
    label_nam.place(x=20, y=110, width=100, height=20)

    label_tt = Label(window_quanLySanPham, text="So Luong")
    label_tt.place(x=20, y=140, width=100, height=20)

    entry_idsach = Entry(window_quanLySanPham)
    entry_idsach.place(x=110, y=20, width=100, height=20)

    entry_tensach = Entry(window_quanLySanPham)
    entry_tensach.place(x=110, y=50, width=100, height=20)

    entry_tacgia = Entry(window_quanLySanPham)
    entry_tacgia.place(x=110, y=80, width=100, height=20)

    entry_nam = Entry(window_quanLySanPham)
    entry_nam.place(x=110, y=110, width=100, height=20)

    entry_tt = Entry(window_quanLySanPham)
    entry_tt.place(x=110, y=140, width=100, height=20)

    button_them = Button(window_quanLySanPham, text="Them", command=themsach)
    button_them.place(x=40, y=170, width=50, height=20)

    button_sua = Button(window_quanLySanPham, text="Sua", command=suasanpham)
    button_sua.place(x=100, y=170, width=50, height=20)

    button_xoa = Button(window_quanLySanPham, text="Xoa", command=xoasanpham)
    button_xoa.place(x=160, y=170, width=50, height=20)

    button_TimKiem = Button(window_quanLySanPham, text="Tim Kiem", command=timKiem)
    button_TimKiem.place(x=220, y=170, width=80, height=20)

    list_sach = Listbox(window_quanLySanPham)
    list_sach.place(x=40, y=200, width=200, height=100)

    mycursor.execute("SELECT * FROM book")
    for x in mycursor.fetchall():
        list_sach.insert(0, str(x))


def quanLyTraMuonSach():
    def muonSach():
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


    window_quanLySanPham = Tk()
    window_quanLySanPham.title("Quan Ly Muon Tra")
    window_quanLySanPham.geometry("350x400")

    label_id = Label(window_quanLySanPham, text="Ma sach")
    label_id.place(x=10, y=20, width=100, height=20)

    label_nguoim= Label(window_quanLySanPham, text="Nguoi muon")
    label_nguoim.place(x=10, y=50, width=100, height=20)

    label_nm = Label(window_quanLySanPham, text="Ngay muon")
    label_nm.place(x=10, y=80, width=100, height=20)

    label_nt = Label(window_quanLySanPham, text="Ngay tra")
    label_nt.place(x=10, y=110, width=100, height=20)

    entry_id = Entry(window_quanLySanPham)
    entry_id.place(x=120, y=20, width=100, height=20)

    entry_nguoim = Entry(window_quanLySanPham)
    entry_nguoim.place(x=120, y=50, width=100, height=20)

    entry_nm = Entry(window_quanLySanPham)
    entry_nm.place(x=120, y=80, width=100, height=20)

    entry_nt = Entry(window_quanLySanPham)
    entry_nt.place(x=120, y=110, width=100, height=20)

    button_muon = Button(window_quanLySanPham, text="Sach muon", command=muonSach)
    button_muon.place(x=40, y=150, width=70, height=20)

    button_tra = Button(window_quanLySanPham, text="Sach tra")
    button_tra.place(x=140, y=150, width=70, height=20)

    list_KhachHang = Listbox(window_quanLySanPham)
    list_KhachHang.place(x=40, y=200, width=200, height=100)

    cursor.execute("SELECT * FROM khachhang")
    for x in cursor.fetchall():
        list_KhachHang.insert(0, x)


button_sanpham = Button(window_quanlymuaban, text="Quan Ly Sach", command=thuVien)
button_sanpham.place(x=10, y=10, width=200, height=20)

button_khachhang = Button(window_quanlymuaban, text="Quan Ly Muon Tra Sach", command=quanLyTraMuonSach)
button_khachhang.place(x=10, y=30, width=200, height=20)
button_Thoat = Button(window_quanlymuaban, text="Thoat", command=exit)
button_Thoat.place(x=10, y=50, width=200, height=20)

window_quanlymuaban.mainloop()
