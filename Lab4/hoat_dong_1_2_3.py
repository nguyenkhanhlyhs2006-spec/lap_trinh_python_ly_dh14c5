#hoat_dong_1
#bai1.1
sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem_tb"))
print(sinh_vien.get("lop", "Chua co"))

#bai1.2
sinh_vien["lop"] = "CNTT01" 
sinh_vien["diem_tb"] = 9.0 
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"})
print(sinh_vien)

#hoat_dong_2
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
for mon in diem_mon_hoc.keys():
 print(mon)
for diem in diem_mon_hoc.values():
 print(diem)
for mon, diem in diem_mon_hoc.items():
 print(f"{mon}: {diem}")
tong_diem = 0
for diem in diem_mon_hoc.values():
 tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#hoat_dong_3
#bai_3.1
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print(mon_hoc_ky1 & mon_hoc_ky2) 
print(mon_hoc_ky1 | mon_hoc_ky2) 

print(mon_hoc_ky1 - mon_hoc_ky2)