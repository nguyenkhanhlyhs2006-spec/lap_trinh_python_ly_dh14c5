# Bai 1.1 

ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

# Bai 1.2 

print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")
# Bai 1.3 
# Cach 1: f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# Cach 2: str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
    ho_ten, nam_sinh, diem_tb
))
# Cach 3: toan tu %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" %
      (ho_ten, nam_sinh, diem_tb))
ho_ten = "Nguyen Khanh Ly" # bien luu ho ten
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
