import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from Class.HakAkses import HakAkses
from Database.Orm.PemeriksaanOrm import PemeriksaanOrm
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse


class MainMenuView(QWidget):
    def __init__(self, username, hakakses):
        super().__init__()

        self.showMaximized()
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle("MAIN MENU")

        # ========== SIDEBAR SECTION =============
        frameSideBar = QFrameReuse("white")
        frameSideBar.setContentsMargins(10, 10, 10, 10)

        sideBarLayout = QGridLayout(frameSideBar)
        sideBarLayout.setSpacing(5)
        btnMainMenu = QPushButtonReuse("Main Menu", "assets/img/medication.png")
        self.btnPasien = QPushButtonReuse("Form.Pasien", "assets/img/pasien.png")
        self.btnDokter = QPushButtonReuse("Form.Dokter", "assets/img/dokter.png")
        self.btnApoteker = QPushButtonReuse("Form.Apoteker", "assets/img/apoteker.png")
        self.btnObat = QPushButtonReuse("Form.Obat", "assets/img/obat.png")
        self.btnUser = QPushButtonReuse("Form.User", "assets/img/user.png")
        self.btnLogOut = QPushButtonReuse("Log Out", "assets/img/log_out.png")

        # =========== EVENT SECTION =============
        self.btnLogOut.clicked.connect(lambda: self.logOutSlot())
        self.btnPasien.clicked.connect(lambda: self.pasienSlot())
        self.btnDokter.clicked.connect(lambda: self.dokterSlot())
        self.btnApoteker.clicked.connect(lambda: self.apotekerSlot())
        self.btnObat.clicked.connect(lambda: self.obatSlot())
        self.btnUser.clicked.connect(lambda: self.userSlot())

        # ========== DASHBOARD SECTION TITLE ===========
        frameTitle = QFrameReuse("white")

        headerLayout = QGridLayout(frameTitle)
        self.hakAkses = QLabelReuse(str(hakakses), "black")

        self.hakAkses.setAlignment(QtCore.Qt.AlignLeft)

        layoutRightTitle = QHBoxLayout()
        self.btnnotification = QPushButtonReuse(str(PemeriksaanOrm.countNotif()), "assets/img/notification.png")
        self.btnnotification.setStyleSheet("background-color : transparent;\n"
                                           "color : red")
        profile = QPushButtonReuse("", "assets/img/profile.png")

        # =========== TITLE SECTION EVENT ============
        self.btnnotification.clicked.connect(lambda: self.pemeriksaanNotif())

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

        self.framePemeriksaan = QFrameReuse("white")
        layoutPemeriksaan = QVBoxLayout(self.framePemeriksaan)
        layoutPemeriksaan.setContentsMargins(45, 45, 45, 45)

        lblPemeriksaan = QLabelReuse("", "")
        lblPemeriksaan.setPixmap(QtGui.QPixmap("assets/img/medical-tool.png"))
        lblPemeriksaan.setAlignment(QtCore.Qt.AlignCenter)
        lblPemeriksaanjudul = QLabelReuse("\nForm. Pemeriksaan\n", "black")
        lblPemeriksaanjudul.setAlignment(QtCore.Qt.AlignCenter)
        self.btnPemeriksaan = QPushButtonReuse("Get Started", "")

        self.frameTransaksi = QFrameReuse("white")
        layoutTransaksi = QVBoxLayout(self.frameTransaksi)
        layoutTransaksi.setContentsMargins(45, 45, 45, 45)

        lblTransaksi = QLabelReuse("", "")
        lblTransaksi.setPixmap(QtGui.QPixmap("assets/img/transaksi.png"))
        lblTransaksi.setAlignment(QtCore.Qt.AlignCenter)
        lblTransaksijudul = QLabelReuse("\nForm. Transaksi\n", "black")
        lblTransaksijudul.setAlignment(QtCore.Qt.AlignCenter)
        self.btnTransaksi = QPushButtonReuse("Get Started", "")

        # ========== DASHBOARD BODY EVENT =========
        self.btnPemeriksaan.clicked.connect(lambda: self.pemeriksaanSlot())

        # ========== LAYOUT SECTION ==============
        sideBarLayout.addWidget(btnMainMenu, 0, 0)
        sideBarLayout.addWidget(self.btnPasien, 1, 0)
        sideBarLayout.addWidget(self.btnDokter, 2, 0)
        sideBarLayout.addWidget(self.btnApoteker, 3, 0)
        sideBarLayout.addWidget(self.btnObat, 4, 0)
        sideBarLayout.addWidget(self.btnUser, 5, 0)
        sideBarLayout.addWidget(self.btnLogOut, 6, 0, QtCore.Qt.AlignBottom)

        layoutRightTitle.addWidget(self.btnnotification)
        layoutRightTitle.addWidget(profile)

        headerLayout.addWidget(self.hakAkses, 0, 0, QtCore.Qt.AlignLeft)
        headerLayout.addLayout(layoutRightTitle, 0, 2, QtCore.Qt.AlignRight)

        frameLayout.addLayout(frameLayoutLeft)
        frameLayout.addLayout(frameLayoutRight)

        frameLayoutLeft.addWidget(welcome)
        frameLayoutLeft.addWidget(self.username)
        frameLayoutLeft.addWidget(quote)

        frameLayoutRight.addWidget(lbllogo)

        layoutPemeriksaan.addWidget(lblPemeriksaan)
        layoutPemeriksaan.addWidget(lblPemeriksaanjudul)
        layoutPemeriksaan.addWidget(self.btnPemeriksaan)

        layoutTransaksi.addWidget(lblTransaksi)
        layoutTransaksi.addWidget(lblTransaksijudul)
        layoutTransaksi.addWidget(self.btnTransaksi)

        layoutUtama = QGridLayout()
        layoutUtama.addWidget(frameSideBar, 0, 0, 6, 1, QtCore.Qt.AlignLeft)
        layoutUtama.addWidget(frameTitle, 0, 1, 1, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameDashboard, 1, 1, 3, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(self.framePemeriksaan, 4, 1, 2, 2, QtCore.Qt.AlignHCenter)
        layoutUtama.addWidget(self.frameTransaksi, 4, 3, 2, 2, QtCore.Qt.AlignHCenter)
        layoutUtama.setSpacing(10)
        self.hakAksesVisible()
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

    @pyqtSlot()
    def obatSlot(self):
        from View.ObatView import ObatView
        self.obatView = ObatView()
        self.obatView.show()
        self.obatView.exec_()

    @pyqtSlot()
    def userSlot(self):
        from View.UserView import UserView
        self.userView = UserView()
        self.userView.show()
        self.userView.exec_()

    @pyqtSlot()
    def pemeriksaanSlot(self):
        from View.PemeriksaanView import PemeriksaanView
        self.periksaView = PemeriksaanView()
        self.periksaView.show()
        self.periksaView.exec_()

    @pyqtSlot()
    def pemeriksaanNotif(self):
        from View.notificationView import notificationView
        self.notifView = notificationView()
        self.notifView.show()
        self.notifView.exec_()

    def hakAksesVisible(self):
        hakAkses = self.hakAkses.text()
        if (hakAkses == str(HakAkses.DOKTER)):
            self.btnUser.setVisible(False)
            self.btnObat.setVisible(False)
            self.btnApoteker.setVisible(False)
            self.btnDokter.setVisible(False)
            self.btnPasien.setVisible(False)
            self.framePemeriksaan.setVisible(False)
            self.frameTransaksi.setVisible(False)
        elif (hakAkses == str(HakAkses.APOTEKER)):
            self.btnUser.setVisible(False)
            self.btnnotification.setVisible(False)
            self.btnApoteker.setVisible(False)
            self.btnDokter.setVisible(False)
            self.btnPasien.setVisible(False)
            self.framePemeriksaan.setVisible(False)
            self.frameTransaksi.setVisible(False)
        else:
            self.btnnotification.setVisible(False)
