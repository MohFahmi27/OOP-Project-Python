from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame


class QFrameReuse(QFrame):

    def __init__(self, colorName):
        super().__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setStyleSheet(
            "background: "+colorName+";\n"
            "border : none;\n"
            "border-radius : 10px;\n")
        self.setContentsMargins(25, 25, 25, 25)

