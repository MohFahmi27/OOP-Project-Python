from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class QPushButtonReuse(QPushButton):

    def __init__(self, text):
        super().__init__()
        self.setStyleSheet("background-color : rgb(0, 85, 255);\n"
                           "border : none;\n"
                           "border-radius : 5px;\n"
                           "height : 50%;\n"
                           "color : white;")
        self.setText(text)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.setFont(font)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
