import sys

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QApplication

from Database.Orm.UserOrm import UserOrm
from View.ReuseComponent.QLabelReuse import QLabelReuse
from View.ReuseComponent.QTableViewModel import QTableViewModel
from View.ReuseComponent.QTableViewReuse import QTableViewReuse


class UserContentView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("USER VIEW")
        self.resize(750, 350)

        lbljudul = QLabelReuse("", "")

        header = ["IDUSER", "USERNAME", "PASSWORD", "HAKAKSES"]
        self.tableModelUser = QTableViewModel(self, header)
        self.tableViewUser = QTableViewReuse()
        self.tableViewUser.setModel(self.tableModelUser)

        layoutUtama = QVBoxLayout(self)
        layoutUtama.addWidget(lbljudul)
        layoutUtama.addWidget(self.tableViewUser)

        self.setLayout(layoutUtama)

app = QApplication(sys.argv)
usercntetn = UserContentView()
usercntetn.show()
sys.exit(app.exec_())