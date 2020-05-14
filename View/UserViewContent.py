import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout

from Database.Orm.UserOrm import UserOrm
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QTableWidgetReuse import QTableWidgetReuse


class UserContentView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("USER VIEW")
        self.resize(750, 350)

        data = UserOrm.showUser()
        iduser, username, password, hakAkses = [], [], [], []

        for i in data:
            iduser = iduser + [i[0]]
            username = username + [i[1]]
            password = password + [i[2]]
            hakAkses = hakAkses + [i[3]]

        result = {'ID USER': iduser, 'USERNAME': username, 'PASSWORD': password, 'HAK AKSES': hakAkses}

        lbljudul = QLabelReuse("DATA USER", "")
        lbljudul.setAlignment(QtCore.Qt.AlignCenter)

        self.tableWidgetUser = QTableWidgetReuse(result, len(data), 4)

        layoutUtama = QVBoxLayout(self)
        layoutUtama.addWidget(lbljudul)
        layoutUtama.addWidget(self.tableWidgetUser)

        self.setLayout(layoutUtama)
