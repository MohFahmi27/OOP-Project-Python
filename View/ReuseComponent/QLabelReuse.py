from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class QLabelReuse(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setWordWrap(True)

        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.setFont(font)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)