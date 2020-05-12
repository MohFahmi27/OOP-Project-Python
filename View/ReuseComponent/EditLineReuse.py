from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class EditLineReuse(QLineEdit):

    def __init__(self, placeholder):
        super().__init__()
        self.setStyleSheet("border : 0;\n"
                           "outline : 0;\n"
                           "background : transparent;\n"
                           "border-bottom : 2px solid rgb(0, 85, 255);")
        self.setPlaceholderText(placeholder)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        font.setWeight(55)

        self.setFont(font)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
