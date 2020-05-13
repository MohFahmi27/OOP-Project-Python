import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QGridLayout, QMessageBox

from Class.Dokter import Dokter
from Database.Orm.DokterOrm import DokterOrm
from View.FormView import FormView
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse


class DokterView(FormView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DOKTER FORM")

        # ========= THIRD LAYOUT =========
        framelayout3 = QFrameReuse("white")
        framelayout3.setContentsMargins(25, 25, 25, 25)
        layout3 = QGridLayout(framelayout3)

        lbljudul3 = QLabelReuse("Data Dokter", "rgb(0, 85, 255)")

        lblspesialis = QLabelReuse("\nSpesialis", "grey")
        lblspesialis.setFont(self.font)
        self.txtspesialis = EditLineReuse("")

        # ========== EVENT SECTION =========
        self.btnTambah.clicked.connect(lambda: self.insertData())

        # =========== LAYOUT SECTION ========
        layout3.addWidget(lbljudul3, 0, 0, 1, 3, Qt.AlignLeft)
        layout3.addWidget(lblspesialis, 1, 0, 1, 3, Qt.AlignLeft)
        layout3.addWidget(self.txtspesialis, 2, 0, 2, 3)

        self.layoutUtama.addWidget(framelayout3, 3, 0, 1, 9)

    @pyqtSlot()
    def insertData(self):
        super(DokterView, self).insertData()
        self.spesialis = self.txtspesialis.text()
        dokter = Dokter(self.nama, self.alamat, self.jenisKelamin, self.noTelp, self.tanggalLahir, self.spesialis)
        try:
            DokterOrm.insertDokter(dokter)
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
        super(DokterView, self).clear()
        self.txtspesialis.setText("")
        self.txtnama.setFocus()
