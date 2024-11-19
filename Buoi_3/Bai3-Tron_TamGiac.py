import math
print("Tính chu vi và diện tích hình tròn, hình tam giác. Kiểm tra điều kiện của chúng.")
print("Tinh chu vi, dien tich hinh tron")
r = float(input("Nhap vao ban kinh hinh tron : "))
if r > 0:
    C = 2*math.pi*r
    print("Chu vi hinh tron la", C)
    S = (C*C)/(4*math.pi)
    print("Dien tich hinh tron la", S)
else:
    print("hay chay lai chuong trinh day khong phai la ban kinh mot duong tron")
print("Tinh chu vi, dien tich tam giac")
a= float(input("Nhap vao canh a : "))
b= float(input("Nhap vao canh b : "))
c= float(input("Nhap vao canh c : "))
if a+b > c and b+c > a and c+a > b:
    C2 = a+b+c
    print("Chu vi tam giac la :", C2)
    p = C2/2
    S2 = p*(p-a)*(p-b)*(p-c)
    print("Dien tich tam giac la", S2)
else:
    print("hay chay lai chuong trinh da khong phai 3 canh cua tam giac")
