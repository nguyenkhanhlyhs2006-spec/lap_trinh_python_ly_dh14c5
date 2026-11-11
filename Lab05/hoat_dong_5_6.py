
# ==========================================
# HOAT DONG 5: PASS, BREAK, CONTINUE
# ==========================================

# Bai tap 5.1 - pass

diem = 6.5

if diem >= 8.0:
    pass
elif diem >= 5.0:
    print("Dat yeu cau")
else:
    pass


# Bai tap 5.2 - break: Kiem tra so nguyen to

so = 29
la_so_nguyen_to = True

if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break

print(f"{so} co phai so nguyen to khong? {la_so_nguyen_to}")


# Bai tap 5.3 - Tim so nguyen to dau tien lon hon n

n = 20
so_hien_tai = n + 1

while True:
    la_so_nguyen_to = True

    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        break

    so_hien_tai += 1

print(f"So nguyen to dau tien lon hon {n} la: {so_hien_tai}")


# Bai tap 5.4 - continue: Loc phan tu hop le

danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []

for so in danh_sach:
    if so <= 0:
        continue

    danh_sach_hop_le.append(so)

print("Cac so hop le (duong):", danh_sach_hop_le)


# ==========================================
# HOAT DONG 6: VONG LAP LONG NHAU
# ==========================================

# Bai tap 6.1 - In tam giac sao

n = 5

print("Tam giac sao:")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


# Bai tap 6.2 - In hinh thoi sao

n = 4

print("Hinh thoi sao:")

# Nua tren cua hinh thoi

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Nua duoi cua hinh thoi

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
