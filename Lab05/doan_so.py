
# ==========================================
# MINI PROJECT: TRO CHOI DOAN SO
# ==========================================

import random

# May chon ngau nhien mot so tu 1 den 100

so_can_doan = random.randint(1, 100)

# So luot doan toi da

so_luot_toi_da = 7
luot_hien_tai = 0

print("================================")
print("       TRO CHOI DOAN SO")
print("================================")
print("May da chon mot so tu 1 den 100.")
print("Ban co toi da 7 luot de doan.")
print("Hay thu tai nao!")

# Vong lap cho nguoi choi doan so

while luot_hien_tai < so_luot_toi_da:

    luot_hien_tai += 1

    so_doan = int(input(
        f"Luot {luot_hien_tai}/{so_luot_toi_da} - "
        "Nhap so ban doan (1-100): "
    ))

    if so_doan == so_can_doan:
        print(
            f"Chinh xac! Ban da doan dung sau "
            f"{luot_hien_tai} luot."
        )
        break

    elif so_doan < so_can_doan:
        print("Goi y: So can doan LON HON so ban vua nhap")

    else:
        print("Goi y: So can doan NHO HON so ban vua nhap")

else:
    print("Ban da het luot doan!")
    print(f"So can tim la: {so_can_doan}")

print("================================")
print("        KET THUC TRO CHOI")
print("================================")
