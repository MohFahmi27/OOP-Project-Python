import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuseTwo import QPushButtonReuseTwo


class MainMenuView(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1400, 833)
        self.setWindowTitle("MAIN MENU")

        # ========== SIDEBAR SECTION =============
        frameSideBar = QFrameReuse("white")
        frameSideBar.setContentsMargins(10, 10, 10, 10)

        sideBarLayout = QGridLayout(frameSideBar)
        sideBarLayout.setSpacing(5)
        btnMainMenu = QPushButtonReuseTwo("", "assets/img/medication.png")
        btnPasien = QPushButtonReuseTwo("", "assets/img/pasien.png")
        btnDokter = QPushButtonReuseTwo("", "assets/img/dokter.png")
        btnApoteker = QPushButtonReuseTwo("", "assets/img/apoteker.png")
        btnObat = QPushButtonReuseTwo("", "assets/img/obat.png")
        btnUser = QPushButtonReuseTwo("", "assets/img/user.png")
        btnLogOut = QPushButtonReuseTwo("", "assets/img/log_out.png")

        # ========== DASHBOARD SECTION TITLE ===========
        frameTitle = QFrameReuse("white")

        headerLayout = QGridLayout(frameTitle)
        hakAkses = QLabelReuse("hak_akses")
        hakAkses.setAlignment(QtCore.Qt.AlignLeft)
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
        welcome = QLabelReuse("Welcome")
        welcome.setFont(font)
        welcome.setStyleSheet("color : white")
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setWeight(75)
        username = QLabelReuse("username")
        username.setStyleSheet("color : white")
        username.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Arial Rounded")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(50)
        quote = QLabelReuse("\n\n\n\n\nTo keep the body in good health is a duty.. otherwise \n\n"
                            "we shall not be able to keep our mind strong and clear.\n")
        quote.setStyleSheet("color : white")
        quote.setFont(font)

        lbllogo = QLabelReuse("")
        lbllogo.setPixmap(QtGui.QPixmap("assets/img/medical256.png"))
        lbllogo.setAlignment(QtCore.Qt.AlignRight)

        # ========== LAYOUT SECTION ==============
        sideBarLayout.addWidget(btnMainMenu, 0, 0)
        sideBarLayout.addWidget(btnPasien, 1, 0)
        sideBarLayout.addWidget(btnDokter, 2, 0)
        sideBarLayout.addWidget(btnApoteker, 3, 0)
        sideBarLayout.addWidget(btnObat, 4, 0)
        sideBarLayout.addWidget(btnUser, 5, 0)
        sideBarLayout.addWidget(btnLogOut, 6, 0, QtCore.Qt.AlignBottom)

        headerLayout.addWidget(hakAkses, 0, 0, QtCore.Qt.AlignLeft)
        headerLayout.addWidget(profile, 0, 2, QtCore.Qt.AlignRight)

        frameLayout.addLayout(frameLayoutLeft)
        frameLayout.addLayout(frameLayoutRight)

        frameLayoutLeft.addWidget(welcome)
        frameLayoutLeft.addWidget(username)
        frameLayoutLeft.addWidget(quote)

        frameLayoutRight.addWidget(lbllogo)

        layoutUtama = QGridLayout()
        layoutUtama.addWidget(frameSideBar, 0, 0, 6, 1, QtCore.Qt.AlignLeft)
        layoutUtama.addWidget(frameTitle, 0, 1, 1, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameDashboard, 1, 1, 5, 9, QtCore.Qt.AlignTop)
        layoutUtama.setSpacing(10)
        self.setLayout(layoutUtama)


app = QApplication(sys.argv)
mainMenuView = MainMenuView()
mainMenuView.show()
sys.exit(app.exec())
