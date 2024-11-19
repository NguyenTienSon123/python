import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MiMi"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE MiMi")

# mycursor.execute("CREATE TABLE taikhoan ("
#                  "mataikhoan INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "sodienthoai INT(10) NOT NULL,"
#                  "matkhau VARCHAR(30) NOT NULL,"
#                  "hovaten VARCHAR(50) NOT NULL,"
#                  "diachi VARCHAR(40) NOT NULL,"
#                  "trangthai INT(1),"
#                  "level INT(1)"
#                  ");")
# mycursor.execute("CREATE TABLE loaimathang ("
#                  "maloaimathang INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "tenloaimathang VARCHAR(100) NOT NULL"
#                  ");")
# mycursor.execute("CREATE TABLE donhang ("
#                  "madonhang INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "mataikhoan INT(6) UNSIGNED,"
#                  "FOREIGN KEY (mataikhoan) REFERENCES taikhoan(mataikhoan)"
#                  ");")
#
# mycursor.execute("CREATE TABLE mathang ("
#                  "mamathang INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "maloaimathang INT(6) UNSIGNED,"
#                  "tenmathang VARCHAR(100) NOT NULL,"
#                  "gia INT(4) NOT NULL,"
#                  "trangthai INT(1),"
#                  "FOREIGN KEY (maloaimathang) REFERENCES loaimathang(maloaimathang)"
#                  ");")
#
# mycursor.execute("CREATE TABLE chitietdonhang ("
#                  "machitietdonhang INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "madonhang INT(6) UNSIGNED,"
#                  "mamathang INT(6) UNSIGNED,"
#                  "soluong INT(5) NOT NULL,"
#                  "FOREIGN KEY (madonhang) REFERENCES donhang(madonhang),"
#                  "FOREIGN KEY (mamathang) REFERENCES mathang(mamathang)"
#                  ");")

# mycursor.execute("CREATE TABLE giohang ("
#                  "magiohang INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "mamathang INT(6) UNSIGNED,"
#                  "mataikhoan INT(6) UNSIGNED,"
#                  "soluong INT(5) NOT NULL,"
#                  "FOREIGN KEY (mataikhoan) REFERENCES taikhoan(mataikhoan),"
#                  "FOREIGN KEY (mamathang) REFERENCES mathang(mamathang)"
#                  ");")