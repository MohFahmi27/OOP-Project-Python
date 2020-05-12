# from PyQt5.QtWidgets import *
# import sys
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1136, 833)
        self.setWindowTitle("LOGIN PUSKESMAS")

        # =========== LAYOUT 1 SECTION ===========
        lbllogo = QLabelReuse("","")
        lbllogo.setPixmap(QtGui.QPixmap("assets/img/lung.svg"))
        lbllogo.setAlignment(QtCore.Qt.AlignCenter)
        lblPresentBy = QLabelReuse("PRESENT BY", "black")
        lblPresentBy.setAlignment(QtCore.Qt.AlignCenter)
        lblCredit = QLabelReuse("-> Mohammad Fahmi         -> Pramana Ade Putra\n"
                                "-> M.Rizqi Nugraha        -> Sakti Pujo Edi", "grey")
        lblCredit.setAlignment(QtCore.Qt.AlignCenter)

        # =========== LAYOUT 2 SECTION ===========
        lbljudul = QLabelReuse("PUSKESMAS", "black")
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(50)
        lbljudul.setFont(font)
        lbljudul.setAlignment(QtCore.Qt.AlignCenter)

        lblusername = QLabelReuse("Username", "grey")
        lblpassword = QLabelReuse("Password", "grey")
        # EditLine
        txtUsername = EditLineReuse("")
        txtpassword = EditLineReuse("")
        txtpassword.setEchoMode(QLineEdit.Password)
        # QPushButton
        btnLogin = QPushButtonReuse("Login")

        # =========== LAYOUT SECTION =============
        layout1 = QVBoxLayout()
        layout1.addWidget(lbllogo)
        layout1.addWidget(lblPresentBy)
        layout1.addWidget(lblCredit)

        layout2 = QVBoxLayout()
        layout2.setContentsMargins(45, 45, 45, 45)
        layout2.setSpacing(0)
        layout2.addWidget(lbljudul)
        layout2.addWidget(lblusername)
        layout2.addWidget(txtUsername)
        layout2.addWidget(lblpassword)
        layout2.addWidget(txtpassword)
        layout2.addWidget(btnLogin)

        layoutUtama = QHBoxLayout()
        layoutUtama.addLayout(layout1)
        layoutUtama.addLayout(layout2)

        self.setLayout(layoutUtama)


app = QApplication(sys.argv)
loginView = LoginView()
loginView.show()
sys.exit(app.exec())
