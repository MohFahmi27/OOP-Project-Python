# from PyQt5.QtWidgets import *
# import sys
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from Database.Orm.UserOrm import UserOrm
from View.MainMenuView import MainMenuView
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1136, 833)
        self.setWindowTitle("LOGIN PUSKESMAS")

        # =========== LAYOUT 1 SECTION ===========
        lbllogo = QLabelReuse("", "")
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
        self.txtUsername = EditLineReuse("")
        self.txtpassword = EditLineReuse("")
        self.txtpassword.setEchoMode(QLineEdit.Password)
        # QPushButton
        self.btnLogin = QPushButtonReuse("Login")
        self.btnLogin.clicked.connect(lambda: self.buttonClick())

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
        layout2.addWidget(self.txtUsername)
        layout2.addWidget(lblpassword)
        layout2.addWidget(self.txtpassword)
        layout2.addWidget(self.btnLogin)

        layoutUtama = QHBoxLayout()
        layoutUtama.addLayout(layout1)
        layoutUtama.addLayout(layout2)

        self.setLayout(layoutUtama)
        self.show()

    @pyqtSlot()
    def buttonClick(self):
        username = self.txtUsername.text()
        password = self.txtpassword.text()
        checkLogin = UserOrm.verifyUser(username, password)
        if (checkLogin == True):
            self.switchMainMenu()
        else:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username Atau Password Salah!")
            msg.setWindowTitle("LOGIN SALAH")
            msg.exec_()

    @pyqtSlot()
    def switchMainMenu(self):
        username = self.txtUsername.text()
        hakAkses = UserOrm.findHakAkses(username)
        self.mainMenu = MainMenuView(username.upper(), hakAkses)
        self.mainMenu.show()
        self.hide()

    def clear(self):
        self.txtUsername.setText("")
        self.txtpassword.setText("")
        self.txtUsername.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginView = LoginView()
    sys.exit(app.exec_())
