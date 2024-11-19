import math
from datetime import date


# 8.    Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại.


def cau8():
    print("Chuyen tu thap phan sang nhi phan")
    a = int(input("Nhap vao so can chuyen doi"))
    bi = []
    while a > 0:
        c = a % 2
        a = int(a / 2)
        bi.append(c)
    bi.reverse()
    while len(bi) < 4:
        bi.insert(0,0)
    for i in bi:
        print(i, end="")
    print("\nChuyen tu nhi phan sang thap phan")
    socu = 0
    bi.reverse()
    for i in range(len(bi)):
        if bi[i] == 1:
            socu += 2**i
    print(socu)
# 10.  Tìm số xuất hiện nhiều và ít nhất trong một danh sách.


def cau10():
    a = int(input("Nhap vao so phan tu cua list"))
    sos = []
    for i in range(a):
        print("nhap vao phan tu thu ", i)
        n = int(input())
        sos.append(n)
    b = []
    c = []
    c2 = []
    for i in sos:
        b.append(sos.count(i))
    for i in range(len(b)):
        if b[i] == max(b):
            c.append(sos[i])
        if b[i] == min(b):
            c2.append(sos[i])

    print('gia tri xuat hien nhieu nhat = ', c[0])
    print('gia tri xuat hien it nhat = ', c2[0])
# 14.    Viết chương trình đọc số, ví dụ nhập 1 hiển thị là Một (sử dụng switch).


def cau14():
    x = int(input("Nhap vao so co hai so chu so"))
    if 0 < x and x < 1000:
        tram = int(x / 100)
        chuc = int((x % 100) / 10)
        match tram:
            case 1:
                print("Mot tram ")
            case 2:
                print("Hai tram ")
            case 3:
                print("Ba tram ")
            case 4:
                print("Bon tram ")
            case 5:
                print("Nam tram ")
            case 6:
                print("Sau tram ")
            case 7:
                print("Bay tram ")
            case 8:
                print("Tam tram ")
            case 9:
                print("Chin tram ")
        match chuc:
            case 1:
                print("Muoi ")
            case 2:
                print("Hai muoi ")
            case 3:
                print("Ba muoi ")
            case 4:
                print("Bon muoi ")
            case 5:
                print("Nam muoi ")
            case 6:
                print("Sau muoi ")
            case 7:
                print("Bay muoi ")
            case 8:
                print("Tam muoi ")
            case 9:
                print("Chin muoi ")
        match (x % 100) % 10:
            case 1:
                print("Mot")
            case 2:
                print("Hai")
            case 3:
                print("Ba")
            case 4:
                print("Bon")
            case 5:
                print("Nam")
            case 6:
                print("Sau")
            case 7:
                print("Bay")
            case 8:
                print("Tam")
            case 9:
                print("Chin")
    else:
        print("So nhap vao khong dung")
# main


chon = input("Moi ban chon")
match chon:
    case "8":
        cau8()
    case "10":
        cau10()
    case "14":
        cau14()
