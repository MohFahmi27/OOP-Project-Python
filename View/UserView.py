from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QGridLayout, QMessageBox, QHBoxLayout

from Class.HakAkses import HakAkses
from Class.User import User
from Database.Orm.UserOrm import UserOrm
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QComboBoxReuse import QComboBoxReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse


class UserView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("USER FORM.")
        self.setModal(True)
        self.resize(1400, 350)

        # ======== FONT CONFIGURE ======
        self.font = QtGui.QFont()
        self.font.setFamily("Product Sans")
        self.font.setPointSize(12)
        self.font.setWeight(55)

        # ======== BASE SECTION ========
        self.layoutUtama = QGridLayout()

        # ======== FIRST LAYOUT =======
        framelayout1 = QFrameReuse("white")
        framelayout1.setContentsMargins(25, 25, 25, 25)
        layout1 = QGridLayout(framelayout1)

        lbljudul = QLabelReuse("Data User", "rgb(0, 85, 255)")

        lblusername = QLabelReuse("\nUsername\n", "grey")
        lblusername.setFont(self.font)
        self.txtusername = EditLineReuse("")

        lblpassword = QLabelReuse("\n\nPassword\n", "grey")
        lblpassword.setFont(self.font)
        self.txtpassword = EditLineReuse("")

        lblhakAkses = QLabelReuse("\nHak Akses\n", "grey")
        lblhakAkses.setFont(self.font)
        self.cmbhakAkses = QComboBoxReuse()
        self.cmbhakAkses.addItems(['DOKTER', 'APOTEKER'])
        self.pilHakAkses = [HakAkses.DOKTER, HakAkses.APOTEKER]

        # ======== CRUD BUTTON ===========
        frameCrudSection = QFrameReuse("white")
        frameCrudSection.setContentsMargins(5, 5, 5, 5)

        layoutCrudSection = QHBoxLayout(frameCrudSection)

        self.btnTambah = QPushButtonReuse("", "assets/img/button.png")
        self.btnTambah.setStyleSheet("background-color : rgb(0, 85, 255);\n"
                                     "height : 80%;\n")
        self.btnTambah.setIconSize(QtCore.QSize(75, 54))

        self.btnView = QPushButtonReuse("", "assets/img/view62.png")
        self.btnView.setStyleSheet("background-color : rgb(0, 85, 255);\n"
                                   "height : 80%;\n")
        self.btnView.setIconSize(QtCore.QSize(75, 54))

        # ========== EVENT SECTION =========
        self.btnTambah.clicked.connect(lambda: self.insertData())
        self.btnView.clicked.connect(lambda: self.viewDataEvent())

        # ======== LAYOUT SECTION ======
        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignVCenter)
        self.layoutUtama.addWidget(frameCrudSection, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lblusername, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtusername, 2, 0, 2, 3)
        layout1.addWidget(lblpassword, 4, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtpassword, 5, 0, 2, 3)
        layout1.addWidget(lblhakAkses, 1, 5, 1, 3)
        layout1.addWidget(self.cmbhakAkses, 2, 5, 2, 3)

        layoutCrudSection.addWidget(self.btnView)
        layoutCrudSection.addWidget(self.btnTambah)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.username = self.txtusername.text()
        self.password = self.txtpassword.text()
        self.hakAkses = self.pilHakAkses[self.cmbhakAkses.currentIndex()]
        user = User(self.username, self.password, self.hakAkses)
        try:
            UserOrm.insertUser(user)
        except Exception as e:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Something Wrong", e)
            msg.setWindowTitle("GAGAL")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Berhasil Di Input!")
            msg.setWindowTitle("BERHASIL")
            msg.exec_()
            self.clear()

    @pyqtSlot()
    def viewDataEvent(self):
        from View.Content.UserContentView import UserContentView
        self.viewData = UserContentView()
        self.viewData.show()
        self.viewData.exec_()

    def clear(self):
        self.txtusername.setText("")
        self.txtpassword.setText("")
        self.cmbhakAkses.setCurrentIndex(0)
        self.txtusername.setFocus()
