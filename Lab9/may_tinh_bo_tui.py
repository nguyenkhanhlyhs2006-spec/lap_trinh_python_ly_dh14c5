
import tkinter as tk
from tkinter import messagebox

def bam_nut(ky_tu):
    hien_tai = bien_hien_thi.get()

    if hien_tai == "Loi":
        bien_hien_thi.set("")

    bien_hien_thi.set(bien_hien_thi.get() + ky_tu)


def xoa():
    bien_hien_thi.set("")


def tinh_ket_qua():
    bieu_thuc = bien_hien_thi.get()

    try:
        ky_tu_hop_le = "0123456789+-*/.() "

        if not bieu_thuc or any(
            ky_tu not in ky_tu_hop_le for ky_tu in bieu_thuc
        ):
            raise ValueError

        ket_qua = eval(bieu_thuc, {"__builtins__": {}}, {})

        bien_hien_thi.set(str(ket_qua))

    except ZeroDivisionError:
        bien_hien_thi.set("Loi chia cho 0")

    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le")


cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

bien_hien_thi = tk.StringVar()

o_hien_thi = tk.Entry(
    cua_so,
    textvariable=bien_hien_thi,
    font=("Arial", 20),
    justify="right",
    state="readonly"
)
o_hien_thi.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=15, ipady=10
)

danh_sach_nut = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]
hang = 1
cot = 0

for nut in danh_sach_nut:
    if nut == "=":
        lenh = tinh_ket_qua
    else:
        lenh = lambda ky_tu=nut: bam_nut(ky_tu)

    tk.Button(
        cua_so,
        text=nut,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lenh
    ).grid(row=hang, column=cot, padx=3, pady=3)

    cot += 1

    if cot == 4:
        cot = 0
        hang += 1

tk.Button(
    cua_so,
    text="C",
    font=("Arial", 16),
    width=23,
    height=2,
    command=xoa
).grid(
    row=5, column=0, columnspan=4,
    padx=5, pady=5
)
if __name__ == "__main__":
    cua_so.mainloop()
