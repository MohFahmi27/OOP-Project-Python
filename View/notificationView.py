import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout

from Database.Orm.PemeriksaanOrm import PemeriksaanOrm
from Database.Orm.UserOrm import UserOrm
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QTableWidgetReuse import QTableWidgetReuse


class notificationView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NOTIFICATION VIEW")
        self.resize(550, 350)

        data = PemeriksaanOrm.showNotif()
        namaPasien, namaDokter, tglPeriksa, status = [], [], [], []

        for i in data:
            namaDokter = namaDokter + [i[0]]
            namaPasien = namaPasien + [i[1]]
            tglPeriksa = tglPeriksa + [i[2]]
            status = status + [i[3]]

        result = {'NAMA DOKTER': namaDokter, 'NAMA PASIEN': namaPasien, 'TANGGAL PERIKSA': tglPeriksa, 'STATUS': status}

        self.tableWidgetNotif = QTableWidgetReuse(result, len(data), 4)

        layoutUtama = QVBoxLayout(self)
        layoutUtama.addWidget(self.tableWidgetNotif)
        self.setLayout(layoutUtama)
