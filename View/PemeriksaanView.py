import sys
from datetime import date

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot

from Class.Pasien import Pasien
from Class.Pemeriksaan import Pemeriksaan
from Database.Orm.DokterOrm import DokterOrm
from Database.Orm.PasienOrm import PasienOrm
from Database.Orm.PemeriksaanOrm import PemeriksaanOrm
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QComboBoxReuse import QComboBoxReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuse import QPushButtonReuse


class PemeriksaanView(QDialog):
    def __init__(self):
        super(PemeriksaanView, self).__init__()
        self.setWindowTitle("PEMERIKSAAN FORM")

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

        lbljudul = QLabelReuse("Data Pemeriksaan", "rgb(0, 85, 255)")

        lblpasien = QLabelReuse("\nPilih Pasien\n", "grey")
        lblpasien.setFont(self.font)
        itempasien = PasienOrm.showPasienIdNama()
        self.cmbpasien = QComboBoxReuse()
        for idpasien,namapasien in itempasien:
            self.cmbpasien.addItem(idpasien+" "+ namapasien, idpasien)

        lblalamat = QLabelReuse("\n\nStatus Pemeriksaan\n", "grey")
        lblalamat.setFont(self.font)
        self.txtalamat = EditLineReuse("")
        self.txtalamat.setText("BELUM DIPERIKSA")
        self.txtalamat.setEnabled(False)

        lbldokter = QLabelReuse("\nPilih Dokter\n", "grey")
        lbldokter.setFont(self.font)
        itemdokter = DokterOrm.showDokterIdNama()

        self.cmbdokter = QComboBoxReuse()
        for id, nama in itemdokter:
            self.cmbdokter.addItem(id +" "+ nama, id)

        lbltanggalLahir = QLabelReuse("\n\nTanggal Pemeriksaan\n", "grey")
        lbltanggalLahir.setFont(self.font)
        self.dateTglLahir = QDateEdit()
        self.dateTglLahir.setStyleSheet("border : 0;\n"
                                        "outline : 0;\n"
                                        "border-bottom : 2px solid rgb(0, 85, 255);")
        self.dateTglLahir.setDisplayFormat("dd - MMM - yyyy")
        self.dateTglLahir.setDate(date.today())
        self.dateTglLahir.setEnabled(False)
        font2 = QtGui.QFont()
        font2.setFamily("Product Sans")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.dateTglLahir.setFont(font2)

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

        # ======== LAYOUT SECTION ======
        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignTop)
        self.layoutUtama.addWidget(frameCrudSection, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)
        self.layoutUtama.setContentsMargins(35, 35, 35, 35)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lblpasien, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.cmbpasien, 2, 0, 2, 3)
        layout1.addWidget(lblalamat, 4, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtalamat, 5, 0, 2, 3)
        layout1.addWidget(lbldokter, 1, 5, 1, 3)
        layout1.addWidget(self.cmbdokter, 2, 5, 2, 3)
        layout1.addWidget(lbltanggalLahir, 4, 5, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.dateTglLahir, 5, 5, 2, 3)

        layoutCrudSection.addWidget(self.btnView)
        layoutCrudSection.addWidget(self.btnTambah)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.pasien = self.cmbpasien.itemData(self.cmbpasien.currentIndex())
        self.dokter = self.cmbdokter.itemData(self.cmbdokter.currentIndex())
        self.status = self.txtalamat.text()
        pemeriksaan = Pemeriksaan(self.pasien, self.dokter, self.status)
        try:
            PemeriksaanOrm.insertPemeriksaan(pemeriksaan)
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