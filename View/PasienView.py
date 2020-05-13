import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from View.FormView import FormView


class PasienView(FormView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASIEN FORM")

