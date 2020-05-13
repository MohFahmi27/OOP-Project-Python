import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QComboBoxReuse import QComboBoxReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse
from View.ReuseComponent.QPushButtonReuseTwo import QPushButtonReuseTwo


class FormView(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1233, 750)
        self.setModal(True)

        # ======== FONT CONFIGURE ======
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setWeight(55)

        # ======== BASE SECTION ========
        self.layoutUtama = QGridLayout()

        # ======== FIRST LAYOUT =======
        framelayout1 = QFrameReuse("white")
        framelayout1.setContentsMargins(25, 25, 25, 25)
        layout1 = QGridLayout(framelayout1)

        lbljudul = QLabelReuse("Data Diri", "rgb(0, 85, 255)")

        lblnama = QLabelReuse("\nNama Lengkap\n", "grey")
        lblnama.setFont(font)
        self.txtnama = EditLineReuse("")

        lblalamat = QLabelReuse("\n\nAlamat\n", "grey")
        lblalamat.setFont(font)
        self.txtalamat = EditLineReuse("")

        lbljenisKelamin = QLabelReuse("\nJenis Kelamin\n", "grey")
        lbljenisKelamin.setFont(font)
        self.cmbJenisKelamin = QComboBoxReuse()

        lbltanggalLahir = QLabelReuse("\n\nTanggal Lahir\n", "grey")
        lbltanggalLahir.setFont(font)
        self.dateTglLahir = QDateEdit()
        self.dateTglLahir.setStyleSheet("border : 0;\n"
                                        "outline : 0;\n"
                                        "background : transparent;\n"
                                        "border-bottom : 2px solid rgb(0, 85, 255);")
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
        lblnoHp.setFont(font)
        txtnoHp = EditLineReuse("+62")

        # ======== ADD DATA ===========
        btnTambah = QPushButtonReuseTwo("", "assets/img/button.png")
        btnTambah.setStyleSheet("background-color : rgb(0, 85, 255);\n"
                                "border : none;\n"
                                "border-radius : 10px;\n"
                                "height : 80%;\n"
                                "color : white;\n")
        btnTambah.setIconSize(QtCore.QSize(75, 54))

        # ======== LAYOUT SECTION ======

        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignTop)
        self.layoutUtama.addWidget(framelayout2, 2, 0, 1, 9)
        self.layoutUtama.addWidget(btnTambah, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)
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
        layout2.addWidget(txtnoHp, 2, 0, 2, 3)

        self.setLayout(self.layoutUtama)
        self.show()
