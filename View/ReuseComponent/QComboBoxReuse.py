from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox


class QComboBoxReuse(QComboBox):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("border : 0;\n"
                           "outline : 0;\n"
                           # "background : transparent;\n"
                           "border-bottom : 2px solid rgb(0, 85, 255);")
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
