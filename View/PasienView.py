import sys

from PyQt5.QtWidgets import QApplication

from View.FormView import FormView


class PasienView(FormView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASIEN FORM")

app = QApplication(sys.argv)
mainMenuView = PasienView()
mainMenuView.show()
sys.exit(app.exec())