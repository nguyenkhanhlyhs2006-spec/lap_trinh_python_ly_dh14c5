
# ==========================================
# HOAT DONG 3: VONG LAP FOR
# ==========================================

# Bai tap 3.1 - For voi range()

print("Cac so tu 1 den 5:")

for i in range(1, 6):
    print(i)


# Bai tap 3.2 - For duyet List

diem_so = [8.5, 7.0, 9.2, 6.5]

print("Danh sach diem:")

for diem in diem_so:
    print("Diem:", diem)


# Bai tap 3.3 - For duyet Tuple

toa_do = (3, 5)

print("Toa do:")

for gia_tri in toa_do:
    print(gia_tri)


# Bai tap 3.4 - For duyet Dictionary

diem_mon = {
    "Toan": 8.0,
    "Ly": 7.5
}

print("Diem cac mon hoc:")

for mon, diem in diem_mon.items():
    print(mon, "-", diem)


# Bai tap 3.5 - For duyet String

ten = "Python"

print("Cac ky tu trong chuoi:")

for ky_tu in ten:
    print(ky_tu)


# Bai tap van dung - Bang cuu chuong

n = 5

print("Bang cuu chuong", n)

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ==========================================
# HOAT DONG 4: VONG LAP WHILE
# ==========================================

# Bai tap 4.1 - Tinh giai thua cua n

n = 5
giai_thua = 1
i = 1

while i <= n:
    giai_thua = giai_thua * i
    i += 1

print(f"{n}! = {giai_thua}")


# Bai tap 4.2 - Tinh tong cac chu so cua mot so

so = 4527
so_tam = so
tong_chu_so = 0

while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10

print(f"Tong cac chu so cua {so} la: {tong_chu_so}")
