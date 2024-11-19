print("Tính chi phí sinh hoạt hàng tháng của bạn")
cackhoan = []
print("Nhap vao cac khoan chi tieu cua ban (Nhap 1 neu khong con khoan nao) : ")
for i in range (20):
    khoan = input()
    if khoan == "1":
        break
    else:
        cackhoan.append(khoan)
print(cackhoan)
tiens = []
tong = 0
for i in cackhoan:
    print("tien chi cho khoan ", i)
    tien = float(input())
    tong = tong + tien
    tiens.append(tien)
for i in range (len(cackhoan)):
    print("khoan      ", "So tien")
    print(cackhoan[i], "  ", tiens[i])
print("Vay thang nay ban dung het ", tong, "vao cac khoan tren")

