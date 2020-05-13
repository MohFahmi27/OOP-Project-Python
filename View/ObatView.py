from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QGridLayout, QMessageBox

from Class.InventarisObat import InventarisObat
from Class.JenisObat import JenisObat
from Class.Obat import Obat
from Database.Orm.InventarisObatOrm import InventarisObatOrm
from Database.Orm.ObatOrm import ObatOrm
from View.ReuseComponent.EditLineReuse import EditLineReuse
from View.ReuseComponent.QComboBoxReuse import QComboBoxReuse
from View.ReuseComponent.QFrameReuse import QFrameReuse
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QPushButtonReuseTwo import QPushButtonReuseTwo


class ObatView(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1400, 700)
        self.setWindowTitle("FORM OBAT")
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

        lbljudul = QLabelReuse("Data Obat", "rgb(0, 85, 255)")

        lblnamaObat = QLabelReuse("\nNama Obat\n", "grey")
        lblnamaObat.setFont(self.font)
        self.txtnamaObat = EditLineReuse("")

        lbljenisObat = QLabelReuse("\nJenis Obat\n", "grey")
        lbljenisObat.setFont(self.font)
        self.cmbJenisObat = QComboBoxReuse()
        self.cmbJenisObat.addItems(['SERBUK', 'TABLET', 'PIL', 'KAPSUL',
                                       'SYRUP', 'SALEP', 'INJEKSI'])
        self.pilJenObat = [JenisObat.SERBUK, JenisObat.TABLET, JenisObat.PIL,
                         JenisObat.KAPSUL, JenisObat.SYRUP,
                         JenisObat.SALEP, JenisObat.INJEKSI]

        # ======== SECOND LAYOUT =======
        framelayout2 = QFrameReuse("white")
        framelayout2.setContentsMargins(25, 25, 25, 25)
        layout2 = QGridLayout(framelayout2)

        lbljudul2 = QLabelReuse("Inventaris Obat", "rgb(0, 85, 255)")

        lblstockObat = QLabelReuse("\nStock Obat", "grey")
        lblstockObat.setFont(self.font)
        self.txtstockObat = EditLineReuse("")

        lblhargaObat = QLabelReuse("\nHarga Obat", "grey")
        lblhargaObat.setFont(self.font)
        self.txthargaObat = EditLineReuse("")

        lbllokasiObat = QLabelReuse("\nLokasi Penyimpanan", "grey")
        lbllokasiObat.setFont(self.font)
        self.txtlokasiObat = EditLineReuse("")

        # ======== ADD DATA ===========
        self.btnTambah = QPushButtonReuseTwo("", "assets/img/button.png")
        self.btnTambah.setStyleSheet("background-color : rgb(0, 85, 255);\n"
                                     "height : 80%;\n")
        self.btnTambah.setIconSize(QtCore.QSize(75, 54))

        # ========== EVENT SECTION =========
        self.btnTambah.clicked.connect(lambda: self.insertData())

        # ======== LAYOUT SECTION ======
        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignTop)
        self.layoutUtama.addWidget(framelayout2, 2, 0, 1, 9)
        self.layoutUtama.addWidget(self.btnTambah, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lbljenisObat, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.cmbJenisObat, 2, 0, 2, 3)
        layout1.addWidget(lblnamaObat, 1, 5, 1, 3)
        layout1.addWidget(self.txtnamaObat, 2, 5, 2, 3)

        layout2.addWidget(lbljudul2, 0, 0, 1, 3, Qt.AlignLeft)
        layout2.addWidget(lblstockObat, 1, 0, 1, 3, Qt.AlignLeft)
        layout2.addWidget(self.txtstockObat, 2, 0, 2, 3)
        layout2.addWidget(lblhargaObat, 4, 0, 1, 3, Qt.AlignLeft)
        layout2.addWidget(self.txthargaObat, 5, 0, 2, 3)
        layout2.addWidget(lbllokasiObat, 1, 5, 1, 3)
        layout2.addWidget(self.txtlokasiObat, 2, 5, 1, 3)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.jenisObat = self.pilJenObat[self.cmbJenisObat.currentIndex()]
        self.namaObat = self.txtnamaObat.text()
        self.stockObat = self.txtstockObat.text()
        self.hargaObat = self.txthargaObat.text()
        self.lokasi = self.txtlokasiObat.text()
        obat = Obat(self.jenisObat, self.namaObat)
        try:
            ObatOrm.insertObat(obat)
        except Exception as e:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Something Wrong", e)
            msg.setWindowTitle("GAGAL")
            msg.exec_()
        else:
            try :
                idObat = ObatOrm.findLatest()
                inv = InventarisObat(idObat, self.stockObat, self.hargaObat, self.lokasi)
                InventarisObatOrm.insertInvenObat(inv)
            except Exception as e:
                msg = QMessageBox()
                msg.resize(250, 250)
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Something Wrong", e)
                msg.setWindowTitle("GAGAL")
                msg.exec_()
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Berhasil Di Input!")
            msg.setWindowTitle("BERHASIL")
            msg.exec_()
            self.clear()

    def clear(self):
        self.txtnamaObat.setText("")
        self.txtstockObat.setText("")
        self.cmbJenisObat.setCurrentIndex(0)
        self.txtlokasiObat.setText("")
        self.txthargaObat.setText("")
        self.txtnamaObat.setFocus()


