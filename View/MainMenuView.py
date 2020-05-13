import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuseTwo import QPushButtonReuseTwo


class MainMenuView(QWidget):
    def __init__(self, username, hakakses):
        super().__init__()
        self.resize(1400, 833)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle("MAIN MENU")

        # ========== SIDEBAR SECTION =============
        frameSideBar = QFrameReuse("white")
        frameSideBar.setContentsMargins(10, 10, 10, 10)

        sideBarLayout = QGridLayout(frameSideBar)
        sideBarLayout.setSpacing(5)
        btnMainMenu = QPushButtonReuseTwo("", "assets/img/medication.png")
        self.btnPasien = QPushButtonReuseTwo("", "assets/img/pasien.png")
        self.btnDokter = QPushButtonReuseTwo("", "assets/img/dokter.png")
        self.btnApoteker = QPushButtonReuseTwo("", "assets/img/apoteker.png")
        self.btnObat = QPushButtonReuseTwo("", "assets/img/obat.png")
        self.btnUser = QPushButtonReuseTwo("", "assets/img/user.png")
        self.btnLogOut = QPushButtonReuseTwo("", "assets/img/log_out.png")

        # =========== EVENT SECTION =============
        self.btnLogOut.clicked.connect(lambda: self.logOutSlot())
        self.btnPasien.clicked.connect(lambda: self.pasienSlot())
        self.btnDokter.clicked.connect(lambda: self.dokterSlot())
        self.btnApoteker.clicked.connect(lambda: self.apotekerSlot())

        # ========== DASHBOARD SECTION TITLE ===========
        frameTitle = QFrameReuse("white")

        headerLayout = QGridLayout(frameTitle)
        self.hakAkses = QLabelReuse(str(hakakses), "black")
        self.hakAkses.setAlignment(QtCore.Qt.AlignLeft)
        profile = QPushButtonReuseTwo("", "assets/img/profile.png")

        # ========== DASHBOARD SECTION BODY ===========
        frameDashboard = QFrameReuse("rgb(58, 150, 248)")
        frameLayout = QHBoxLayout(frameDashboard)
        frameLayout.setContentsMargins(40, 40, 40, 40)

        frameLayoutLeft = QVBoxLayout()
        frameLayoutRight = QVBoxLayout()

        font = QtGui.QFont()
        font.setFamily("Arial Rounded")
        font.setPointSize(11)
        font.setWeight(50)
        welcome = QLabelReuse("Welcome", "white")
        welcome.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setWeight(75)
        self.username = QLabelReuse(username, "white")
        self.username.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Arial Rounded")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(50)
        quote = QLabelReuse("\n\n\n\n\nTo keep the body in good health is a duty.. otherwise \n\n"
                            "we shall not be able to keep our mind strong and clear.\n", "white")
        quote.setFont(font)

        lbllogo = QLabelReuse("", "")
        lbllogo.setPixmap(QtGui.QPixmap("assets/img/medical256.png"))
        lbllogo.setAlignment(QtCore.Qt.AlignRight)

        # ========== LAYOUT SECTION ==============
        sideBarLayout.addWidget(btnMainMenu, 0, 0)
        sideBarLayout.addWidget(self.btnPasien, 1, 0)
        sideBarLayout.addWidget(self.btnDokter, 2, 0)
        sideBarLayout.addWidget(self.btnApoteker, 3, 0)
        sideBarLayout.addWidget(self.btnObat, 4, 0)
        sideBarLayout.addWidget(self.btnUser, 5, 0)
        sideBarLayout.addWidget(self.btnLogOut, 6, 0, QtCore.Qt.AlignBottom)

        headerLayout.addWidget(self.hakAkses, 0, 0, QtCore.Qt.AlignLeft)
        headerLayout.addWidget(profile, 0, 2, QtCore.Qt.AlignRight)

        frameLayout.addLayout(frameLayoutLeft)
        frameLayout.addLayout(frameLayoutRight)

        frameLayoutLeft.addWidget(welcome)
        frameLayoutLeft.addWidget(self.username)
        frameLayoutLeft.addWidget(quote)

        frameLayoutRight.addWidget(lbllogo)

        layoutUtama = QGridLayout()
        layoutUtama.addWidget(frameSideBar, 0, 0, 6, 1, QtCore.Qt.AlignLeft)
        layoutUtama.addWidget(frameTitle, 0, 1, 1, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameDashboard, 1, 1, 5, 9, QtCore.Qt.AlignTop)
        layoutUtama.setSpacing(10)
        self.setLayout(layoutUtama)

    @pyqtSlot()
    def logOutSlot(self):
        from View.LoginView import LoginView
        self.login = LoginView()
        self.login.show()
        self.close()

    @pyqtSlot()
    def pasienSlot(self):
        from View.PasienView import PasienView
        self.pasienview = PasienView()
        self.pasienview.show()
        self.pasienview.exec_()

    @pyqtSlot()
    def dokterSlot(self):
        from View.DokterView import DokterView
        self.dokterView = DokterView()
        self.dokterView.show()
        self.dokterView.exec_()

    @pyqtSlot()
    def apotekerSlot(self):
        from View.ApotekerView import ApotekerView
        self.apotekerView = ApotekerView()
        self.apotekerView.show()
        self.apotekerView.exec_()



