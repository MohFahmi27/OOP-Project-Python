from PyQt5 import Qt
from PyQt5.QtCore import QAbstractTableModel, QVariant

from Database.Orm.UserOrm import UserOrm


class QTableViewModel(QAbstractTableModel):

    def __init__(self, parent, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        result = UserOrm.showUserContent()
        self.mylist = result
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        # 5. populate data
        if not index.isValid():
            return None
        if (role == Qt.DisplayRole):
            return self.mylist[index.row()][index.column()]
        else:
            return QVariant()

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
