from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from Database.Orm.UserOrm import UserOrm


class QTableWidgetReuse(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        font.setWeight(55)
        self.setFont(font)

    def setmydata(self):
        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
