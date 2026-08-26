
#3.1
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen)) # ep int -> float
print(int(so_thuc)) # ep float -> int (cat phan thap phan)
#3.2
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a)) # gia tri tuyet doi
print(round(b)) # lam tron
print(round(b, 2)) # lam tron 2 chu so thap phan
print(pow(c, 2)) # c mu 2
print(divmod(c, d)) # tra ve (thuong, du) dang tuple
import math

a = 1
b = -3
c = 2
delta = b ** 2 - 4 * a * c

print(f"Delta = {delta}")
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"Phuong trinh co 2 nghiem phan biet")
    print(f"Nghiem x1 = {round(x1, 2)}")
    print(f"Nghiem x2 = {round(x2, 2)}")

elif delta == 0:
    x = -b / (2 * a)

    print("Phuong trinh co nghiem kep")
    print(f"Nghiem x = {round(x, 2)}")

else:
    print("Phuong trinh vo nghiem")
    
# Bài tập 4.1 - Indexing & Slicing

print("===== BÀI TẬP 4.1 - INDEXING & SLICING =====")

cau = "Lap trinh Python rat thu vi"

print(cau[0])       # ký tự đầu tiên
print(cau[-1])      # ký tự cuối cùng
print(cau[4:10])    # cắt từ vị trí 4 đến trước vị trí 10
print(cau[:8])      # từ đầu đến vị trí 8
print(cau[11:])     # từ vị trí 11 đến hết
print(cau[::-1])    # đảo ngược chuỗi

chuoi = input("Nhập chuỗi cần kiểm tra palindrome: ")

if chuoi == chuoi[::-1]:
    print("Đây là chuỗi palindrome.")
else:
    print("Đây không phải là chuỗi palindrome.")


# Bài tập 4.2 
print("\n===== BÀI TẬP 4.2 - TÍNH BẤT BIẾN =====")

ten = "Nam"
ten_moi = "T" + ten[1:]

print("Tên ban đầu:", ten)
print("Tên mới:", ten_moi)



# Bài tập 4.3 - Các phương thức xử lý chuỗi

print("\n===== BÀI TẬP 4.3 - CÁC PHƯƠNG THỨC XỬ LÝ CHUỖI =====")

cau = "  Toi dang HOC Python rat vui  "

print(cau.strip())                    # bỏ khoảng trắng 2 đầu
print(cau.strip().upper())            # in hoa toàn bộ
print(cau.strip().lower())            # in thường toàn bộ
print(cau.strip().replace("HOC", "hoc"))  # thay thế "HOC" thành "hoc"
print(cau.strip().split())            # tách thành danh sách các từ
print(len(cau.strip().split()))       # đếm số từ trong câu
print(cau.count("o"))                 # đếm số lần xuất hiện ký tự 'o'
print(cau.find("Python"))             # vị trí bắt đầu của "Python"
print(cau.strip().startswith("Toi")) # kiểm tra bắt đầu bằng "Toi"
print(cau.strip().endswith("vui"))   # kiểm tra kết thúc bằng "vui"

print("-".join(["Python", "that", "thu", "vi"]))

# Bài tập 4.4 - Vận dụng: Chuẩn hóa họ tên
print("\n===== BÀI TẬP 4.4 - CHUẨN HÓA HỌ TÊN =====")

ho_ten_tho = "   nguyen   van   an   "

ho_ten_sach = " ".join(ho_ten_tho.split()).title()

print("Họ tên sau khi chuẩn hóa:", ho_ten_sach)