danh_sach_sinh_vien = [
    {
        "ma_sv": "SV01",
        "ho_ten": "Nguyen Van An",
        "tuoi": 20,
        "nganh": "CNTT",
        "diem": 8.5
    },
    {
        "ma_sv": "SV02",
        "ho_ten": "Tran Thi Binh",
        "tuoi": 21,
        "nganh": "Kinh te",
        "diem": 7.5
    },
    {
        "ma_sv": "SV03",
        "ho_ten": "Le Van Cuong",
        "tuoi": 20,
        "nganh": "CNTT",
        "diem": 4.5
    },
    {
        "ma_sv": "SV04",
        "ho_ten": "Pham Thi Dung",
        "tuoi": 22,
        "nganh": "Ke toan",
        "diem": 9.0
    }
]


def hien_thi_danh_sach_sinh_vien():
    print("\n" + "=" * 75)
    print(f"{'Ma SV':<10}{'Ho ten':<20}{'Tuoi':<8}{'Nganh':<15}{'Diem':<10}")
    print("-" * 75)

    for sinh_vien in danh_sach_sinh_vien:
        print(
            f"{sinh_vien['ma_sv']:<10}"
            f"{sinh_vien['ho_ten']:<20}"
            f"{sinh_vien['tuoi']:<8}"
            f"{sinh_vien['nganh']:<15}"
            f"{sinh_vien['diem']:<10}"
        )

    print("=" * 75)


def tim_sinh_vien_theo_ma(ma_sv):
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien["ma_sv"] == ma_sv:
            return sinh_vien

    return None


def xem_sinh_vien_dat():
    sinh_vien_dat = [
        sinh_vien
        for sinh_vien in danh_sach_sinh_vien
        if sinh_vien["diem"] >= 5
    ]

    if len(sinh_vien_dat) == 0:
        print("-> Hien khong co sinh vien nao dat.")
        return

    print("\nCAC SINH VIEN DAT:")

    for sinh_vien in sinh_vien_dat:
        print(
            f" {sinh_vien['ma_sv']} - "
            f"{sinh_vien['ho_ten']} - "
            f"{sinh_vien['diem']} diem"
        )


def them_sinh_vien(ma_sv, ho_ten, tuoi, nganh, diem):
    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return

    danh_sach_sinh_vien.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "nganh": nganh,
        "diem": diem
    })

    print(f"-> Da them sinh vien {ma_sv} thanh cong.")


def cap_nhat_diem(ma_sv, diem_moi):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    sinh_vien["diem"] = diem_moi

    print(f"-> Da cap nhat diem cho sinh vien {ma_sv} thanh cong.")


def xoa_sinh_vien(ma_sv):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    danh_sach_sinh_vien.remove(sinh_vien)

    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")


def thong_ke_diem_trung_binh():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co sinh vien nao.")
        return

    tong_diem = 0

    for sinh_vien in danh_sach_sinh_vien:
        tong_diem += sinh_vien["diem"]

    diem_trung_binh = tong_diem / len(danh_sach_sinh_vien)

    print(f"\n>>> DIEM TRUNG BINH CUA TAT CA SINH VIEN: {diem_trung_binh:.2f}")


def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


def nhap_so_thuc(loi_nhac):
    while True:
        try:
            return float(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so.")


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach tat ca sinh vien")
    print("2. Xem sinh vien dat")
    print("3. Them sinh vien moi")
    print("4. Cap nhat diem sinh vien")
    print("5. Xoa sinh vien")
    print("6. Tim sinh vien theo ma")
    print("7. Thong ke diem trung binh")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_sinh_vien()

        elif lua_chon == "2":
            xem_sinh_vien_dat()

        elif lua_chon == "3":
            ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()
            ho_ten = input("Nhap ho ten sinh vien: ").strip().title()
            tuoi = nhap_so_nguyen("Nhap tuoi: ")
            nganh = input("Nhap nganh hoc: ").strip().title()
            diem = nhap_so_thuc("Nhap diem: ")

            them_sinh_vien(
                ma_sv,
                ho_ten,
                tuoi,
                nganh,
                diem
            )

        elif lua_chon == "4":
            ma_sv = input("Nhap ma sinh vien can cap nhat: ").strip().upper()
            diem_moi = nhap_so_thuc("Nhap diem moi: ")

            cap_nhat_diem(ma_sv, diem_moi)

        elif lua_chon == "5":
            ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()

            xoa_sinh_vien(ma_sv)

        elif lua_chon == "6":
            ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()

            sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

            if sinh_vien is None:
                print(f"-> Khong tim thay sinh vien {ma_sv}.")
            else:
                print("\nTHONG TIN SINH VIEN:")
                print(f"Ma sinh vien: {sinh_vien['ma_sv']}")
                print(f"Ho ten: {sinh_vien['ho_ten']}")
                print(f"Tuoi: {sinh_vien['tuoi']}")
                print(f"Nganh: {sinh_vien['nganh']}")
                print(f"Diem: {sinh_vien['diem']}")

        elif lua_chon == "7":
            thong_ke_diem_trung_binh()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()