import sys

from PyQt5.QtWidgets import QApplication

from View.FormView import FormView


class DokterView(FormView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DOKTER FORM")
