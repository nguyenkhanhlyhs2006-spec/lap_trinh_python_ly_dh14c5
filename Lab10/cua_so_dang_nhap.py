
import sys
import os

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox
)
from PyQt5 import uic


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        # Lay duong dan thu muc chua file Python
        thu_muc = os.path.dirname(os.path.abspath(__file__))

        # Tao duong dan den file giao dien
        duong_dan_ui = os.path.join(
            thu_muc,
            "form_dang_nhap.ui"
        )

        # Tai giao dien tu file UI
        uic.loadUi(duong_dan_ui, self)

        # Ket noi nut dang nhap voi ham xu ly
        self.nut_dang_nhap.clicked.connect(
            self.kiem_tra_dang_nhap
        )

    def kiem_tra_dang_nhap(self):
        # Lay tai khoan va mat khau nguoi dung nhap
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()

        # Kiem tra thong tin dang nhap
        if tai_khoan == "admin" and mat_khau == "123456":
            QMessageBox.information(
                self,
                "Thong bao",
                "Dang nhap thanh cong!"
            )
        else:
            QMessageBox.warning(
                self,
                "Loi dang nhap",
                "Tai khoan hoac mat khau khong dung!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = CuaSoDangNhap()
    cua_so.show()

    sys.exit(app.exec_())
