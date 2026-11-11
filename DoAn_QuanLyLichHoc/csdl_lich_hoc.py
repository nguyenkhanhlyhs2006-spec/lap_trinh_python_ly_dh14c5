
import sqlite3

TEN_FILE_CSDL = "quan_ly_hoc_tap.db"


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    # Bang thoi khoa bieu
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS lich_hoc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_mon TEXT NOT NULL,
            giang_vien TEXT,
            thu TEXT NOT NULL,
            gio_bat_dau TEXT NOT NULL,
            gio_ket_thuc TEXT NOT NULL,
            phong TEXT NOT NULL,
            ghi_chu TEXT
        )
    """)

    # Bang bai tap va cong viec
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS bai_tap (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_cong_viec TEXT NOT NULL,
            noi_dung TEXT,
            han_nop TEXT NOT NULL,
            trang_thai TEXT NOT NULL DEFAULT 'Chua xong'
        )
    """)

    ket_noi.commit()
    ket_noi.close()


# ==========================================
# CAC HAM QUAN LY THOI KHOA BIEU
# ==========================================

def them_lich_hoc(ten_mon, giang_vien, thu,
                  gio_bat_dau, gio_ket_thuc, phong, ghi_chu):

    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        INSERT INTO lich_hoc (
            ten_mon, giang_vien, thu,
            gio_bat_dau, gio_ket_thuc, phong, ghi_chu
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        ten_mon, giang_vien, thu,
        gio_bat_dau, gio_ket_thuc, phong, ghi_chu
    ))

    ket_noi.commit()
    ket_noi.close()


def lay_toan_bo_lich_hoc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT id, ten_mon, giang_vien, thu,
               gio_bat_dau, gio_ket_thuc, phong, ghi_chu
        FROM lich_hoc
        ORDER BY
            CASE thu
                WHEN 'Thu 2' THEN 2
                WHEN 'Thu 3' THEN 3
                WHEN 'Thu 4' THEN 4
                WHEN 'Thu 5' THEN 5
                WHEN 'Thu 6' THEN 6
                WHEN 'Thu 7' THEN 7
                WHEN 'Chu nhat' THEN 8
            END,
            gio_bat_dau
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


def sua_lich_hoc(id_lich, ten_mon, giang_vien, thu,
                 gio_bat_dau, gio_ket_thuc, phong, ghi_chu):

    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        UPDATE lich_hoc
        SET ten_mon = ?,
            giang_vien = ?,
            thu = ?,
            gio_bat_dau = ?,
            gio_ket_thuc = ?,
            phong = ?,
            ghi_chu = ?
        WHERE id = ?
    """, (
        ten_mon, giang_vien, thu,
        gio_bat_dau, gio_ket_thuc,
        phong, ghi_chu, id_lich
    ))

    ket_noi.commit()
    ket_noi.close()


def xoa_lich_hoc(id_lich):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute(
        "DELETE FROM lich_hoc WHERE id = ?",
        (id_lich,)
    )

    ket_noi.commit()
    ket_noi.close()


def lay_lich_theo_thu(thu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT id, ten_mon, giang_vien, thu,
               gio_bat_dau, gio_ket_thuc, phong, ghi_chu
        FROM lich_hoc
        WHERE thu = ?
        ORDER BY gio_bat_dau
    """, (thu,))

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


# ==========================================
# CAC HAM QUAN LY BAI TAP
# ==========================================

def them_bai_tap(ten_cong_viec, noi_dung, han_nop, trang_thai):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        INSERT INTO bai_tap (
            ten_cong_viec, noi_dung, han_nop, trang_thai
        )
        VALUES (?, ?, ?, ?)
    """, (
        ten_cong_viec, noi_dung, han_nop, trang_thai
    ))

    ket_noi.commit()
    ket_noi.close()


def lay_toan_bo_bai_tap():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT id, ten_cong_viec, noi_dung, han_nop, trang_thai
        FROM bai_tap
        ORDER BY han_nop
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


def sua_bai_tap(id_bai_tap, ten_cong_viec,
                noi_dung, han_nop, trang_thai):

    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        UPDATE bai_tap
        SET ten_cong_viec = ?,
            noi_dung = ?,
            han_nop = ?,
            trang_thai = ?
        WHERE id = ?
    """, (
        ten_cong_viec, noi_dung,
        han_nop, trang_thai, id_bai_tap
    ))

    ket_noi.commit()
    ket_noi.close()


def xoa_bai_tap(id_bai_tap):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute(
        "DELETE FROM bai_tap WHERE id = ?",
        (id_bai_tap,)
    )

    ket_noi.commit()
    ket_noi.close()


def cap_nhat_trang_thai(id_bai_tap, trang_thai):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        UPDATE bai_tap
        SET trang_thai = ?
        WHERE id = ?
    """, (trang_thai, id_bai_tap))

    ket_noi.commit()
    ket_noi.close()


def lay_bai_tap_chua_hoan_thanh():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT id, ten_cong_viec, noi_dung, han_nop, trang_thai
        FROM bai_tap
        WHERE trang_thai != 'Hoan thanh'
        ORDER BY han_nop
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


# ==========================================
# CAC HAM THONG KE
# ==========================================

def thong_ke_so_tiet_theo_mon():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT ten_mon,
               SUM(
                   (CAST(substr(gio_ket_thuc, 1, 2) AS INTEGER) * 60
                    + CAST(substr(gio_ket_thuc, 4, 2) AS INTEGER))
                   -
                   (CAST(substr(gio_bat_dau, 1, 2) AS INTEGER) * 60
                    + CAST(substr(gio_bat_dau, 4, 2) AS INTEGER))
               ) / 50.0
        FROM lich_hoc
        GROUP BY ten_mon
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


def thong_ke_so_gio_theo_ngay():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT thu,
               SUM(
                   (CAST(substr(gio_ket_thuc, 1, 2) AS INTEGER) * 60
                    + CAST(substr(gio_ket_thuc, 4, 2) AS INTEGER))
                   -
                   (CAST(substr(gio_bat_dau, 1, 2) AS INTEGER) * 60
                    + CAST(substr(gio_bat_dau, 4, 2) AS INTEGER))
               ) / 60.0
        FROM lich_hoc
        GROUP BY thu
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


def thong_ke_bai_tap():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT trang_thai, COUNT(*)
        FROM bai_tap
        GROUP BY trang_thai
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua
