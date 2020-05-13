import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot

from Class.JenisKelamin import JenisKelamin
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QComboBoxReuse import QComboBoxReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse
from View.ReuseComponent.QPushButtonReuseTwo import QPushButtonReuseTwo


class FormView(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1400, 700)
        self.setModal(True)

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

        lbljudul = QLabelReuse("Data Diri", "rgb(0, 85, 255)")

        lblnama = QLabelReuse("\nNama Lengkap\n", "grey")
        lblnama.setFont(self.font)
        self.txtnama = EditLineReuse("")

        lblalamat = QLabelReuse("\n\nAlamat\n", "grey")
        lblalamat.setFont(self.font)
        self.txtalamat = EditLineReuse("")

        lbljenisKelamin = QLabelReuse("\nJenis Kelamin\n", "grey")
        lbljenisKelamin.setFont(self.font)
        self.cmbJenisKelamin = QComboBoxReuse()
        self.cmbJenisKelamin.addItems(['LAKI_LAKI', 'PEREMPUAN'])
        self.pilJekel = [JenisKelamin.LAKI_LAKI, JenisKelamin.PEREMPUAN]

        lbltanggalLahir = QLabelReuse("\n\nTanggal Lahir\n", "grey")
        lbltanggalLahir.setFont(self.font)
        self.dateTglLahir = QDateEdit()
        self.dateTglLahir.setStyleSheet("border : 0;\n"
                                        "outline : 0;\n"
                                        "background : transparent;\n"
                                        "border-bottom : 2px solid rgb(0, 85, 255);")
        self.dateTglLahir.setDisplayFormat("yyyy, MM, dd")
        font2 = QtGui.QFont()
        font2.setFamily("Product Sans")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.dateTglLahir.setFont(font2)

        # ======== SECOND LAYOUT =======
        framelayout2 = QFrameReuse("white")
        framelayout2.setContentsMargins(25, 25, 25, 25)
        layout2 = QGridLayout(framelayout2)

        lbljudul2 = QLabelReuse("Contact Information", "rgb(0, 85, 255)")

        lblnoHp = QLabelReuse("\nNo Hp", "grey")
        lblnoHp.setFont(self.font)
        self.txtnoHp = EditLineReuse("+62")

        # ======== ADD DATA ===========
        self.btnTambah = QPushButtonReuseTwo("", "assets/img/button.png")
        self.btnTambah.setStyleSheet("background-color : rgb(0, 85, 255);\n"
                                "border : none;\n"
                                "border-radius : 10px;\n"
                                "height : 80%;\n"
                                "color : white;\n")
        self.btnTambah.setIconSize(QtCore.QSize(75, 54))

        # ======== LAYOUT SECTION ======

        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignTop)
        self.layoutUtama.addWidget(framelayout2, 2, 0, 1, 9)
        self.layoutUtama.addWidget(self.btnTambah, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)
        self.layoutUtama.setContentsMargins(35, 35, 35, 35)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lblnama, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtnama, 2, 0, 2, 3)
        layout1.addWidget(lblalamat, 4, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtalamat, 5, 0, 2, 3)
        layout1.addWidget(lbljenisKelamin, 1, 5, 1, 3)
        layout1.addWidget(self.cmbJenisKelamin, 2, 5, 2, 3)
        layout1.addWidget(lbltanggalLahir, 4, 5, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.dateTglLahir, 5, 5, 2, 3)

        layout2.addWidget(lbljudul2, 0, 0, 1, 3, Qt.AlignLeft)
        layout2.addWidget(lblnoHp, 1, 0, 1, 3, Qt.AlignLeft)
        layout2.addWidget(self.txtnoHp, 2, 0, 2, 3)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.nama = self.txtnama.text()
        self.alamat = self.txtalamat.text()
        self.jenisKelamin = self.pilJekel[self.cmbJenisKelamin.currentIndex()]
        self.tanggalLahir = self.dateTglLahir.date().toPyDate()
        self.noTelp = self.txtnoHp.text()

    def clear(self):
        self.txtnama.setText("")
        self.txtalamat.setText("")
        self.cmbJenisKelamin.setCurrentIndex(0)
        self.txtnoHp.setText("")
