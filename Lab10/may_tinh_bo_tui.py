
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QGridLayout, QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt


class MayTinh(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("May tinh bo tui")
        self.setFixedSize(320, 400)

        # Tao giao dien chinh
        layout_chinh = QVBoxLayout()

        # Man hinh hien thi
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setStyleSheet(
            "font-size: 24px; padding: 10px;"
        )
        layout_chinh.addWidget(self.man_hinh)

        # Tao luoi cac nut bam
        layout_nut = QGridLayout()

        danh_sach_nut = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("C", 3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3)
        ]

        for chu, hang, cot in danh_sach_nut:
            nut = QPushButton(chu)
            nut.setMinimumHeight(55)
            nut.setStyleSheet("font-size: 20px;")

            nut.clicked.connect(
                lambda checked=False, gia_tri=chu:
                self.xu_ly_nut(gia_tri)
            )

            layout_nut.addWidget(nut, hang, cot)

        layout_chinh.addLayout(layout_nut)
        self.setLayout(layout_chinh)

    def xu_ly_nut(self, gia_tri):
        if gia_tri == "C":
            self.man_hinh.clear()

        elif gia_tri == "=":
            bieu_thuc = self.man_hinh.text()

            try:
                # Chi cho phep cac ky tu phep tinh co ban
                ky_tu_hop_le = "0123456789+-*/.() "

                if not bieu_thuc or any(
                    ky_tu not in ky_tu_hop_le
                    for ky_tu in bieu_thuc
                ):
                    self.man_hinh.setText("Loi")
                    return

                ket_qua = eval(bieu_thuc, {"__builtins__": {}})

                self.man_hinh.setText(str(ket_qua))

            except ZeroDivisionError:
                self.man_hinh.setText("Khong the chia cho 0")

            except Exception:
                self.man_hinh.setText("Bieu thuc khong hop le")

        else:
            if self.man_hinh.text() in [
                "Loi",
                "Khong the chia cho 0",
                "Bieu thuc khong hop le"
            ]:
                self.man_hinh.clear()

            self.man_hinh.setText(
                self.man_hinh.text() + gia_tri
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = MayTinh()
    cua_so.show()

    sys.exit(app.exec_())
