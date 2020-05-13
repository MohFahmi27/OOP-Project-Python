import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QGridLayout, QMessageBox

from Class.Apoteker import Apoteker
from Database.Orm.ApotekerOrm import ApotekerOrm
from View.FormView import FormView
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse


class ApotekerView(FormView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("APOTEKER FORM")

        # ========= THIRD LAYOUT =========
        framelayout3 = QFrameReuse("white")
        framelayout3.setContentsMargins(25, 25, 25, 25)
        layout3 = QGridLayout(framelayout3)

        lbljudul3 = QLabelReuse("Data Apoteker", "rgb(0, 85, 255)")

        lblnoNip = QLabelReuse("\nNo NIP", "grey")
        lblnoNip.setFont(self.font)
        self.txtnoNip = EditLineReuse("")

        # ========== EVENT SECTION =========
        self.btnTambah.clicked.connect(lambda: self.insertData())

        # =========== LAYOUT SECTION ========
        layout3.addWidget(lbljudul3, 0, 0, 1, 3, Qt.AlignLeft)
        layout3.addWidget(lblnoNip, 1, 0, 1, 3, Qt.AlignLeft)
        layout3.addWidget(self.txtnoNip, 2, 0, 2, 3)

        self.layoutUtama.addWidget(framelayout3, 3, 0, 1, 9)

    @pyqtSlot()
    def insertData(self):
        super(ApotekerView, self).insertData()
        self.noNip = self.txtnoNip.text()
        apoteker = Apoteker(self.nama, self.alamat, self.jenisKelamin, self.noTelp, self.tanggalLahir, self.noNip)
        try:
            ApotekerOrm.insertApoteker(apoteker)
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
        super(ApotekerView, self).clear()
        self.txtnoNip.setText("")
        self.txtnama.setFocus()
