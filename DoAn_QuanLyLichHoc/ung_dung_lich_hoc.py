
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_lich_hoc as db


DANH_SACH_THU = [
    "Thu 2", "Thu 3", "Thu 4",
    "Thu 5", "Thu 6", "Thu 7", "Chu nhat"
]

DANH_SACH_TRANG_THAI = [
    "Chua xong", "Dang lam", "Hoan thanh"
]

THU_TU = {
    "Thu 2": 2,
    "Thu 3": 3,
    "Thu 4": 4,
    "Thu 5": 5,
    "Thu 6": 6,
    "Thu 7": 7,
    "Chu nhat": 8
}


class UngDungLichHoc(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("He thong quan ly hoc tap sinh vien")
        self.geometry("1200x780")
        self.minsize(1050, 700)

        db.tao_bang_neu_chua_co()

        self.id_lich_dang_chon = None
        self.id_bai_tap_dang_chon = None

        self.khoi_tao_giao_dien()
        self.tai_lai_lich_hoc()
        self.tai_lai_bai_tap()


    # ==========================================
    # TAO GIAO DIEN CHUNG
    # ==========================================

    def khoi_tao_giao_dien(self):

        tieu_de = tk.Label(
            self,
            text="QUAN LY HOC TAP SINH VIEN",
            font=("Arial", 20, "bold"),
            fg="blue"
        )
        tieu_de.pack(pady=12)

        self.cac_tab = ttk.Notebook(self)
        self.cac_tab.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=8
        )

        self.tab_lich_hoc = ttk.Frame(self.cac_tab)
        self.tab_bai_tap = ttk.Frame(self.cac_tab)
        self.tab_thong_ke = ttk.Frame(self.cac_tab)

        self.cac_tab.add(
            self.tab_lich_hoc,
            text="Thoi khoa bieu"
        )

        self.cac_tab.add(
            self.tab_bai_tap,
            text="Bai tap va cong viec"
        )

        self.cac_tab.add(
            self.tab_thong_ke,
            text="Thong ke hoc tap"
        )

        self.tao_tab_lich_hoc()
        self.tao_tab_bai_tap()
        self.tao_tab_thong_ke()


    # ==========================================
    # TAB 1: QUAN LY THOI KHOA BIEU
    # ==========================================

    def tao_tab_lich_hoc(self):

        khung_nhap = ttk.LabelFrame(
            self.tab_lich_hoc,
            text="Thong tin lich hoc",
            padding=10
        )
        khung_nhap.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # Ten mon
        ttk.Label(
            khung_nhap,
            text="Ten mon hoc:"
        ).grid(row=0, column=0, sticky="w", pady=6)

        self.o_ten_mon = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_ten_mon.grid(
            row=0, column=1, padx=8, pady=6
        )

        # Giang vien
        ttk.Label(
            khung_nhap,
            text="Giang vien:"
        ).grid(row=0, column=2, sticky="w", pady=6)

        self.o_giang_vien = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_giang_vien.grid(
            row=0, column=3, padx=8, pady=6
        )

        # Thu
        ttk.Label(
            khung_nhap,
            text="Thu:"
        ).grid(row=1, column=0, sticky="w", pady=6)

        self.chon_thu = ttk.Combobox(
            khung_nhap,
            values=DANH_SACH_THU,
            state="readonly",
            width=22
        )
        self.chon_thu.current(0)
        self.chon_thu.grid(
            row=1, column=1, padx=8, pady=6
        )

        # Gio bat dau
        ttk.Label(
            khung_nhap,
            text="Gio bat dau (HH:MM):"
        ).grid(row=1, column=2, sticky="w", pady=6)

        self.o_gio_bat_dau = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_gio_bat_dau.grid(
            row=1, column=3, padx=8, pady=6
        )

        # Gio ket thuc
        ttk.Label(
            khung_nhap,
            text="Gio ket thuc (HH:MM):"
        ).grid(row=2, column=0, sticky="w", pady=6)

        self.o_gio_ket_thuc = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_gio_ket_thuc.grid(
            row=2, column=1, padx=8, pady=6
        )

        # Phong
        ttk.Label(
            khung_nhap,
            text="Phong hoc:"
        ).grid(row=2, column=2, sticky="w", pady=6)

        self.o_phong = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_phong.grid(
            row=2, column=3, padx=8, pady=6
        )

        # Ghi chu
        ttk.Label(
            khung_nhap,
            text="Ghi chu:"
        ).grid(row=3, column=0, sticky="w", pady=6)

        self.o_ghi_chu_lich = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_ghi_chu_lich.grid(
            row=3, column=1, padx=8, pady=6
        )

        # Cac nut thao tac
        khung_nut = ttk.Frame(khung_nhap)
        khung_nut.grid(
            row=3, column=2, columnspan=2, pady=8
        )

        ttk.Button(
            khung_nut,
            text="Them",
            command=self.xu_ly_them_lich
        ).pack(side="left", padx=4)

        ttk.Button(
            khung_nut,
            text="Cap nhat",
            command=self.xu_ly_sua_lich
        ).pack(side="left", padx=4)

        ttk.Button(
            khung_nut,
            text="Xoa",
            command=self.xu_ly_xoa_lich
        ).pack(side="left", padx=4)

        ttk.Button(
            khung_nut,
            text="Lam moi",
            command=self.lam_moi_form_lich
        ).pack(side="left", padx=4)

        # Khung loc theo thu
        khung_loc = ttk.Frame(self.tab_lich_hoc)
        khung_loc.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Label(
            khung_loc,
            text="Xem lich theo thu:"
        ).pack(side="left", padx=5)

        self.loc_thu = ttk.Combobox(
            khung_loc,
            values=["Tat ca"] + DANH_SACH_THU,
            state="readonly",
            width=18
        )
        self.loc_thu.current(0)
        self.loc_thu.pack(side="left", padx=5)

        self.loc_thu.bind(
            "<<ComboboxSelected>>",
            self.loc_lich_theo_thu
        )

        ttk.Button(
            khung_loc,
            text="Xem ca tuan",
            command=self.tai_lai_lich_hoc
        ).pack(side="left", padx=8)

        # Bang thoi khoa bieu
        khung_bang = ttk.LabelFrame(
            self.tab_lich_hoc,
            text="Thoi khoa bieu trong tuan",
            padding=8
        )
        khung_bang.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=8
        )

        cot = (
            "id", "thu", "ten_mon", "giang_vien",
            "thoi_gian", "phong", "ghi_chu"
        )

        self.bang_lich = ttk.Treeview(
            khung_bang,
            columns=cot,
            show="headings",
            height=13
        )

        tieu_de_cot = {
            "id": "ID",
            "thu": "Thu",
            "ten_mon": "Mon hoc",
            "giang_vien": "Giang vien",
            "thoi_gian": "Thoi gian",
            "phong": "Phong hoc",
            "ghi_chu": "Ghi chu"
        }

        do_rong = {
            "id": 40,
            "thu": 90,
            "ten_mon": 190,
            "giang_vien": 160,
            "thoi_gian": 150,
            "phong": 100,
            "ghi_chu": 180
        }

        for ten_cot in cot:
            self.bang_lich.heading(
                ten_cot,
                text=tieu_de_cot[ten_cot]
            )
            self.bang_lich.column(
                ten_cot,
                width=do_rong[ten_cot],
                anchor="center"
            )

        thanh_cuon = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.bang_lich.yview
        )

        self.bang_lich.configure(
            yscrollcommand=thanh_cuon.set
        )

        self.bang_lich.pack(
            side="left",
            fill="both",
            expand=True
        )
        thanh_cuon.pack(side="right", fill="y")

        self.bang_lich.bind(
            "<<TreeviewSelect>>",
            self.chon_lich_hoc
        )


    def lay_thong_tin_lich(self):

        ten_mon = self.o_ten_mon.get().strip()
        giang_vien = self.o_giang_vien.get().strip()
        thu = self.chon_thu.get()
        gio_bat_dau = self.o_gio_bat_dau.get().strip()
        gio_ket_thuc = self.o_gio_ket_thuc.get().strip()
        phong = self.o_phong.get().strip()
        ghi_chu = self.o_ghi_chu_lich.get().strip()

        if not ten_mon or not giang_vien or not phong:
            messagebox.showerror(
                "Loi",
                "Vui long nhap ten mon, giang vien va phong hoc."
            )
            return None

        try:
            bat_dau = datetime.strptime(
                gio_bat_dau, "%H:%M"
            )
            ket_thuc = datetime.strptime(
                gio_ket_thuc, "%H:%M"
            )
        except ValueError:
            messagebox.showerror(
                "Loi",
                "Gio hoc phai co dang HH:MM, vi du 07:00."
            )
            return None

        if ket_thuc <= bat_dau:
            messagebox.showerror(
                "Loi",
                "Gio ket thuc phai sau gio bat dau."
            )
            return None

        return (
            ten_mon, giang_vien, thu,
            gio_bat_dau, gio_ket_thuc,
            phong, ghi_chu
        )


    def tai_lai_lich_hoc(self):

        for dong in self.bang_lich.get_children():
            self.bang_lich.delete(dong)

        danh_sach = db.lay_toan_bo_lich_hoc()

        for lich in danh_sach:
            id_lich, ten_mon, giang_vien, thu, bat_dau, ket_thuc, phong, ghi_chu = lich

            self.bang_lich.insert(
                "",
                tk.END,
                values=(
                    id_lich,
                    thu,
                    ten_mon,
                    giang_vien,
                    bat_dau + " - " + ket_thuc,
                    phong,
                    ghi_chu
                )
            )

        self.loc_thu.current(0)
        self.id_lich_dang_chon = None


    def loc_lich_theo_thu(self, event=None):

        thu = self.loc_thu.get()

        for dong in self.bang_lich.get_children():
            self.bang_lich.delete(dong)

        if thu == "Tat ca":
            danh_sach = db.lay_toan_bo_lich_hoc()
        else:
            danh_sach = db.lay_lich_theo_thu(thu)

        for lich in danh_sach:
            id_lich, ten_mon, giang_vien, thu, bat_dau, ket_thuc, phong, ghi_chu = lich

            self.bang_lich.insert(
                "",
                tk.END,
                values=(
                    id_lich,
                    thu,
                    ten_mon,
                    giang_vien,
                    bat_dau + " - " + ket_thuc,
                    phong,
                    ghi_chu
                )
            )

        self.id_lich_dang_chon = None


    def xu_ly_them_lich(self):

        thong_tin = self.lay_thong_tin_lich()

        if thong_tin is None:
            return

        db.them_lich_hoc(*thong_tin)

        self.tai_lai_lich_hoc()
        self.lam_moi_form_lich()

        messagebox.showinfo(
            "Thanh cong",
            "Da them lich hoc."
        )


    def xu_ly_sua_lich(self):

        if self.id_lich_dang_chon is None:
            messagebox.showerror(
                "Loi",
                "Hay chon lich hoc can sua trong bang."
            )
            return

        thong_tin = self.lay_thong_tin_lich()

        if thong_tin is None:
            return

        db.sua_lich_hoc(
            self.id_lich_dang_chon,
            *thong_tin
        )

        self.tai_lai_lich_hoc()
        self.lam_moi_form_lich()

        messagebox.showinfo(
            "Thanh cong",
            "Da cap nhat lich hoc."
        )


    def xu_ly_xoa_lich(self):

        if self.id_lich_dang_chon is None:
            messagebox.showerror(
                "Loi",
                "Hay chon lich hoc can xoa."
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xac nhan",
            "Ban co chac chan muon xoa lich hoc nay?"
        )

        if not xac_nhan:
            return

        db.xoa_lich_hoc(self.id_lich_dang_chon)

        self.tai_lai_lich_hoc()
        self.lam_moi_form_lich()

        messagebox.showinfo(
            "Thanh cong",
            "Da xoa lich hoc."
        )


    def chon_lich_hoc(self, event=None):

        lua_chon = self.bang_lich.selection()

        if not lua_chon:
            return

        du_lieu = self.bang_lich.item(
            lua_chon[0], "values"
        )

        self.id_lich_dang_chon = int(du_lieu[0])

        danh_sach = db.lay_toan_bo_lich_hoc()

        for lich in danh_sach:
            if lich[0] == self.id_lich_dang_chon:
                self.o_ten_mon.delete(0, tk.END)
                self.o_ten_mon.insert(0, lich[1])

                self.o_giang_vien.delete(0, tk.END)
                self.o_giang_vien.insert(0, lich[2])

                self.chon_thu.set(lich[3])

                self.o_gio_bat_dau.delete(0, tk.END)
                self.o_gio_bat_dau.insert(0, lich[4])

                self.o_gio_ket_thuc.delete(0, tk.END)
                self.o_gio_ket_thuc.insert(0, lich[5])

                self.o_phong.delete(0, tk.END)
                self.o_phong.insert(0, lich[6])

                self.o_ghi_chu_lich.delete(0, tk.END)
                self.o_ghi_chu_lich.insert(0, lich[7] or "")

                break


    def lam_moi_form_lich(self):

        self.id_lich_dang_chon = None

        self.o_ten_mon.delete(0, tk.END)
        self.o_giang_vien.delete(0, tk.END)
        self.chon_thu.current(0)
        self.o_gio_bat_dau.delete(0, tk.END)
        self.o_gio_ket_thuc.delete(0, tk.END)
        self.o_phong.delete(0, tk.END)
        self.o_ghi_chu_lich.delete(0, tk.END)

        for dong in self.bang_lich.selection():
            self.bang_lich.selection_remove(dong)


    # ==========================================
    # TAB 2: QUAN LY BAI TAP VA CONG VIEC
    # ==========================================

    def tao_tab_bai_tap(self):

        khung_nhap = ttk.LabelFrame(
            self.tab_bai_tap,
            text="Thong tin bai tap va cong viec",
            padding=10
        )
        khung_nhap.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            khung_nhap,
            text="Ten cong viec:"
        ).grid(row=0, column=0, sticky="w", pady=6)

        self.o_ten_cong_viec = ttk.Entry(
            khung_nhap,
            width=35
        )
        self.o_ten_cong_viec.grid(
            row=0, column=1, padx=8, pady=6
        )

        ttk.Label(
            khung_nhap,
            text="Han nop (DD/MM/YYYY):"
        ).grid(row=0, column=2, sticky="w", pady=6)

        self.o_han_nop = ttk.Entry(
            khung_nhap,
            width=25
        )
        self.o_han_nop.grid(
            row=0, column=3, padx=8, pady=6
        )

        ttk.Label(
            khung_nhap,
            text="Noi dung:"
        ).grid(row=1, column=0, sticky="w", pady=6)

        self.o_noi_dung = ttk.Entry(
            khung_nhap,
            width=35
        )
        self.o_noi_dung.grid(
            row=1, column=1, padx=8, pady=6
        )

        ttk.Label(
            khung_nhap,
            text="Trang thai:"
        ).grid(row=1, column=2, sticky="w", pady=6)

        self.chon_trang_thai = ttk.Combobox(
            khung_nhap,
            values=DANH_SACH_TRANG_THAI,
            state="readonly",
            width=22
        )
        self.chon_trang_thai.current(0)
        self.chon_trang_thai.grid(
            row=1, column=3, padx=8, pady=6
        )

        khung_nut = ttk.Frame(khung_nhap)
        khung_nut.grid(
            row=2, column=0, columnspan=4, pady=10
        )

        ttk.Button(
            khung_nut,
            text="Them cong viec",
            command=self.xu_ly_them_bai_tap
        ).pack(side="left", padx=5)

        ttk.Button(
            khung_nut,
            text="Cap nhat",
            command=self.xu_ly_sua_bai_tap
        ).pack(side="left", padx=5)

        ttk.Button(
            khung_nut,
            text="Danh dau hoan thanh",
            command=self.xu_ly_hoan_thanh
        ).pack(side="left", padx=5)

        ttk.Button(
            khung_nut,
            text="Xoa cong viec",
            command=self.xu_ly_xoa_bai_tap
        ).pack(side="left", padx=5)

        ttk.Button(
            khung_nut,
            text="Lam moi",
            command=self.lam_moi_form_bai_tap
        ).pack(side="left", padx=5)

        # Loc cong viec
        khung_loc = ttk.Frame(self.tab_bai_tap)
        khung_loc.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Label(
            khung_loc,
            text="Loc cong viec:"
        ).pack(side="left", padx=5)

        self.loc_bai_tap = ttk.Combobox(
            khung_loc,
            values=[
                "Tat ca",
                "Chua hoan thanh",
                "Da hoan thanh"
            ],
            state="readonly",
            width=22
        )
        self.loc_bai_tap.current(0)
        self.loc_bai_tap.pack(side="left", padx=5)

        self.loc_bai_tap.bind(
            "<<ComboboxSelected>>",
            self.loc_danh_sach_bai_tap
        )

        ttk.Button(
            khung_loc,
            text="Xem tat ca",
            command=self.tai_lai_bai_tap
        ).pack(side="left", padx=5)

        # Bang bai tap
        khung_bang = ttk.LabelFrame(
            self.tab_bai_tap,
            text="Danh sach bai tap va cong viec",
            padding=8
        )
        khung_bang.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=8
        )

        cot = (
            "id",
            "ten_cong_viec",
            "noi_dung",
            "han_nop",
            "trang_thai"
        )

        self.bang_bai_tap = ttk.Treeview(
            khung_bang,
            columns=cot,
            show="headings",
            height=15
        )

        tieu_de = {
            "id": "ID",
            "ten_cong_viec": "Cong viec",
            "noi_dung": "Noi dung",
            "han_nop": "Han nop",
            "trang_thai": "Trang thai"
        }

        do_rong = {
            "id": 50,
            "ten_cong_viec": 230,
            "noi_dung": 350,
            "han_nop": 150,
            "trang_thai": 160
        }

        for ten_cot in cot:
            self.bang_bai_tap.heading(
                ten_cot,
                text=tieu_de[ten_cot]
            )
            self.bang_bai_tap.column(
                ten_cot,
                width=do_rong[ten_cot],
                anchor="center"
            )

        self.bang_bai_tap.pack(
            fill="both",
            expand=True
        )

        self.bang_bai_tap.bind(
            "<<TreeviewSelect>>",
            self.chon_bai_tap
        )


    def lay_thong_tin_bai_tap(self):

        ten = self.o_ten_cong_viec.get().strip()
        noi_dung = self.o_noi_dung.get().strip()
        han_nop = self.o_han_nop.get().strip()
        trang_thai = self.chon_trang_thai.get()

        if not ten or not han_nop:
            messagebox.showerror(
                "Loi",
                "Vui long nhap ten cong viec va han nop."
            )
            return None

        try:
            ngay = datetime.strptime(
                han_nop, "%d/%m/%Y"
            )
        except ValueError:
            messagebox.showerror(
                "Loi",
                "Han nop phai co dang DD/MM/YYYY, vi du 15/11/2026."
            )
            return None

        han_nop_luu = ngay.strftime("%Y-%m-%d")

        return ten, noi_dung, han_nop_luu, trang_thai


    def tai_lai_bai_tap(self):

        for dong in self.bang_bai_tap.get_children():
            self.bang_bai_tap.delete(dong)

        danh_sach = db.lay_toan_bo_bai_tap()

        for bai_tap in danh_sach:
            id_bt, ten, noi_dung, han_nop, trang_thai = bai_tap

            ngay_hien_thi = datetime.strptime(
                han_nop, "%Y-%m-%d"
            ).strftime("%d/%m/%Y")

            self.bang_bai_tap.insert(
                "",
                tk.END,
                values=(
                    id_bt,
                    ten,
                    noi_dung,
                    ngay_hien_thi,
                    trang_thai
                )
            )

        self.loc_bai_tap.current(0)
        self.id_bai_tap_dang_chon = None


    def loc_danh_sach_bai_tap(self, event=None):

        lua_chon = self.loc_bai_tap.get()

        if lua_chon == "Tat ca":
            danh_sach = db.lay_toan_bo_bai_tap()

        elif lua_chon == "Chua hoan thanh":
            danh_sach = db.lay_bai_tap_chua_hoan_thanh()

        else:
            danh_sach = [
                bt for bt in db.lay_toan_bo_bai_tap()
                if bt[4] == "Hoan thanh"
            ]

        for dong in self.bang_bai_tap.get_children():
            self.bang_bai_tap.delete(dong)

        for bai_tap in danh_sach:
            id_bt, ten, noi_dung, han_nop, trang_thai = bai_tap

            ngay_hien_thi = datetime.strptime(
                han_nop, "%Y-%m-%d"
            ).strftime("%d/%m/%Y")

            self.bang_bai_tap.insert(
                "",
                tk.END,
                values=(
                    id_bt,
                    ten,
                    noi_dung,
                    ngay_hien_thi,
                    trang_thai
                )
            )


    def xu_ly_them_bai_tap(self):

        thong_tin = self.lay_thong_tin_bai_tap()

        if thong_tin is None:
            return

        db.them_bai_tap(*thong_tin)

        self.tai_lai_bai_tap()
        self.lam_moi_form_bai_tap()

        messagebox.showinfo(
            "Thanh cong",
            "Da them cong viec."
        )


    def xu_ly_sua_bai_tap(self):

        if self.id_bai_tap_dang_chon is None:
            messagebox.showerror(
                "Loi",
                "Hay chon cong viec can cap nhat."
            )
            return

        thong_tin = self.lay_thong_tin_bai_tap()

        if thong_tin is None:
            return

        db.sua_bai_tap(
            self.id_bai_tap_dang_chon,
            *thong_tin
        )

        self.tai_lai_bai_tap()
        self.lam_moi_form_bai_tap()

        messagebox.showinfo(
            "Thanh cong",
            "Da cap nhat cong viec."
        )


    def xu_ly_hoan_thanh(self):

        if self.id_bai_tap_dang_chon is None:
            messagebox.showerror(
                "Loi",
                "Hay chon mot cong viec."
            )
            return

        db.cap_nhat_trang_thai(
            self.id_bai_tap_dang_chon,
            "Hoan thanh"
        )

        self.tai_lai_bai_tap()
        self.lam_moi_form_bai_tap()

        messagebox.showinfo(
            "Thanh cong",
            "Da danh dau cong viec hoan thanh."
        )


    def xu_ly_xoa_bai_tap(self):

        if self.id_bai_tap_dang_chon is None:
            messagebox.showerror(
                "Loi",
                "Hay chon cong viec can xoa."
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xac nhan",
            "Ban co chac chan muon xoa cong viec nay?"
        )

        if not xac_nhan:
            return

        db.xoa_bai_tap(self.id_bai_tap_dang_chon)

        self.tai_lai_bai_tap()
        self.lam_moi_form_bai_tap()

        messagebox.showinfo(
            "Thanh cong",
            "Da xoa cong viec."
        )


    def chon_bai_tap(self, event=None):

        lua_chon = self.bang_bai_tap.selection()

        if not lua_chon:
            return

        du_lieu = self.bang_bai_tap.item(
            lua_chon[0], "values"
        )

        self.id_bai_tap_dang_chon = int(du_lieu[0])

        self.o_ten_cong_viec.delete(0, tk.END)
        self.o_ten_cong_viec.insert(0, du_lieu[1])

        self.o_noi_dung.delete(0, tk.END)
        self.o_noi_dung.insert(0, du_lieu[2])

        self.o_han_nop.delete(0, tk.END)
        self.o_han_nop.insert(0, du_lieu[3])

        self.chon_trang_thai.set(du_lieu[4])


    def lam_moi_form_bai_tap(self):

        self.id_bai_tap_dang_chon = None

        self.o_ten_cong_viec.delete(0, tk.END)
        self.o_noi_dung.delete(0, tk.END)
        self.o_han_nop.delete(0, tk.END)
        self.chon_trang_thai.current(0)

        for dong in self.bang_bai_tap.selection():
            self.bang_bai_tap.selection_remove(dong)


    # ==========================================
    # TAB 3: THONG KE HOC TAP
    # ==========================================

    def tao_tab_thong_ke(self):

        mo_ta = ttk.Label(
            self.tab_thong_ke,
            text=(
                "Thong ke ket qua hoc tap bang bieu do Matplotlib"
            ),
            font=("Arial", 12, "bold")
        )
        mo_ta.pack(pady=25)

        ttk.Button(
            self.tab_thong_ke,
            text="TAO BIEU DO THONG KE",
            command=self.xu_ly_thong_ke
        ).pack(pady=15)

        self.nhan_thong_ke = ttk.Label(
            self.tab_thong_ke,
            text=(
                "Bieu do gom 3 noi dung:\n"
                "1. So tiet hoc theo tung mon.\n"
                "2. So gio hoc theo tung ngay.\n"
                "3. So luong bai tap theo trang thai.\n\n"
                "Nhan nut ben tren de xem va luu bieu do."
            ),
            justify="left",
            font=("Arial", 11)
        )
        self.nhan_thong_ke.pack(pady=20)


    def xu_ly_thong_ke(self):

        du_lieu_mon = db.thong_ke_so_tiet_theo_mon()
        du_lieu_ngay = db.thong_ke_so_gio_theo_ngay()
        du_lieu_bai_tap = db.thong_ke_bai_tap()

        if not du_lieu_mon and not du_lieu_bai_tap:
            messagebox.showinfo(
                "Thong bao",
                "Chua co du lieu de thong ke."
            )
            return

        # Chuan bi du lieu bieu do mon hoc
        mon_hoc = [dong[0] for dong in du_lieu_mon]
        so_tiet = [dong[1] for dong in du_lieu_mon]

        # Chuan bi du lieu bieu do theo ngay
        du_lieu_ngay.sort(
            key=lambda dong: THU_TU.get(dong[0], 9)
        )

        cac_thu = [dong[0] for dong in du_lieu_ngay]
        so_gio = [dong[1] for dong in du_lieu_ngay]

        # Chuan bi du lieu bai tap
        trang_thai = [
            "Chua xong",
            "Dang lam",
            "Hoan thanh"
        ]

        so_luong = []

        for ten_trang_thai in trang_thai:
            so_dem = 0

            for dong in du_lieu_bai_tap:
                if dong[0] == ten_trang_thai:
                    so_dem = dong[1]

            so_luong.append(so_dem)

        # Tao 3 bieu do trong cung mot anh
        fig, cac_truc = plt.subplots(
            1, 3,
            figsize=(17, 5)
        )

        # Bieu do 1: So tiet theo mon
        if mon_hoc:
            cac_truc[0].bar(
                mon_hoc,
                so_tiet,
                color="cornflowerblue"
            )

            cac_truc[0].set_title(
                "So tiet hoc theo mon"
            )
            cac_truc[0].set_xlabel("Mon hoc")
            cac_truc[0].set_ylabel("So tiet")
            cac_truc[0].tick_params(
                axis="x",
                rotation=45
            )
        else:
            cac_truc[0].set_title(
                "Chua co du lieu mon hoc"
            )

        # Bieu do 2: So gio theo ngay
        if cac_thu:
            cac_truc[1].bar(
                cac_thu,
                so_gio,
                color="seagreen"
            )

            cac_truc[1].set_title(
                "So gio hoc theo ngay"
            )
            cac_truc[1].set_xlabel("Thu")
            cac_truc[1].set_ylabel("So gio")
        else:
            cac_truc[1].set_title(
                "Chua co du lieu lich hoc"
            )

        # Bieu do 3: Trang thai bai tap
        cac_truc[2].bar(
            trang_thai,
            so_luong,
            color="orange"
        )

        cac_truc[2].set_title(
            "Thong ke trang thai bai tap"
        )
        cac_truc[2].set_xlabel("Trang thai")
        cac_truc[2].set_ylabel("So luong")

        fig.tight_layout()

        # Luu anh
        duong_dan = (
            Path(__file__).resolve().parent
            / "thong_ke_hoc_tap.png"
        )

        fig.savefig(
            duong_dan,
            dpi=300,
            bbox_inches="tight"
        )

        plt.show()

        self.nhan_thong_ke.config(
            text=(
                "Da tao thanh cong 3 bieu do thong ke.\n\n"
                f"Anh da duoc luu tai:\n{duong_dan}"
            )
        )

        messagebox.showinfo(
            "Thanh cong",
            f"Da luu bieu do tai:\n{duong_dan}"
        )


# ==========================================
# CHAY CHUONG TRINH
# ==========================================

if __name__ == "__main__":

    ung_dung = UngDungLichHoc()
    ung_dung.mainloop()
