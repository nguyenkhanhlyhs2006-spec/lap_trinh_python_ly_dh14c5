import sys
sys.stdout.reconfigure(encoding="utf-8")

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000 
print("Tên học sinh:", ten)
print("Điểm toán:", diem_toan)
print("Điểm văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)
a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
diem = 6.5
tuoi = 20

kiem_tra_diem = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", kiem_tra_diem)

kiem_tra_tuoi = (tuoi < 18) or (tuoi > 60)
print("Tuổi chưa đủ 18 hoặc trên 60:", kiem_tra_tuoi)
x = 10
x += 5  
print("Sau khi += 5, x =", x)


x -= 3   
print("Sau khi -= 3, x =", x)

x *= 2   
print("Sau khi *= 2, x =", x)

x /= 4  
print("Sau khi /= 4, x =", x)

x //= 2 
print("Sau khi //= 2, x =", x)

x **= 3  
print("Sau khi **= 3, x =", x)


danh_sach = [1, 2, 3, "python"]


print("3 có trong danh_sach không?", 3 in danh_sach)


danh_sach_2 = danh_sach  
print("danh_sach_2 is danh_sach:", danh_sach_2 is danh_sach)
print("Phủ định điều kiện tuổi:", not kiem_tra_tuoi)
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)