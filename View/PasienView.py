import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot

from Class.Pasien import Pasien
from Class.User import User
from Database.Orm.PasienOrm import PasienOrm
from View.FormView import FormView
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse


class PasienView(FormView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASIEN FORM")

        # ========= THIRD LAYOUT =========
        framelayout3 = QFrameReuse("white")
        framelayout3.setContentsMargins(25, 25, 25, 25)
        layout3 = QGridLayout(framelayout3)

        lbljudul3 = QLabelReuse("Data Pasien", "rgb(0, 85, 255)")

        lblnoKk = QLabelReuse("\nNo KK", "grey")
        lblnoKk.setFont(self.font)
        self.txtnoKk = EditLineReuse("")
        self.txtnoKk.setValidator(QIntValidator(0, 9999))

        lblnoKtp = QLabelReuse("\nNo KK", "grey")
        lblnoKtp.setFont(self.font)
        self.txtnoKtp = EditLineReuse("")
        self.txtnoKtp.setValidator(QIntValidator(0, 9999))

        # ========== EVENT SECTION =========
        self.btnTambah.clicked.connect(lambda: self.insertData())

        # =========== LAYOUT SECTION ========
        layout3.addWidget(lbljudul3, 0, 0, 1, 3, Qt.AlignLeft)
        layout3.addWidget(lblnoKk, 1, 0, 1, 3, Qt.AlignLeft)
        layout3.addWidget(self.txtnoKk, 2, 0, 2, 3)
        layout3.addWidget(lblnoKtp, 1, 5, 1, 3)
        layout3.addWidget(self.txtnoKtp, 2, 5, 2, 3)

        self.layoutUtama.addWidget(framelayout3, 3, 0, 1, 9)

    @pyqtSlot()
    def insertData(self):
        super(PasienView, self).insertData()
        self.noKk = str(self.txtnoKk.text())
        self.noKtp = str(self.txtnoKtp.text())
        pasien = Pasien(self.nama, self.alamat, self.jenisKelamin, self.noTelp, self.tanggalLahir, self.noKk,
                        self.noKtp)
        try:
            PasienOrm.insertPasien(pasien)
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

    def clear(self):
        super(PasienView, self).clear()
        self.txtnoKtp.setText("")
        self.txtnoKk.setText("")
        self.txtnama.setFocus()
