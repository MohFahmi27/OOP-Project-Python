from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableView


class QTableViewReuse(QTableView):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("border: 2px solid grey;")
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(11)
        font.setWeight(45)