from Class.Obat import Obat
from db.Orm.InventarisObatOrm import InventarisObatOrm
from db.base import sessionFactory


class InventarisObat():

    def __init__(self, idObat, stockObat, expObat, hargaObat, lokasi):
        self.idobat = idObat
        self.stockObat = stockObat
        self.expObat = expObat
        self.hargaObat = hargaObat
        self.lokasi = lokasi

    def insertInventarisObat(self):
        try:
            session = sessionFactory()
            inventarisObatOrm = InventarisObatOrm(self.idobat, self.stockObat, self.expObat, self.hargaObat,
                                                  self.lokasi)
            session.add(inventarisObatOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def showInventarisObat():
        try:
            session = sessionFactory()
            for inv in session.query(InventarisObatOrm).all():
                print("Id = {}\nId Obat = {}\nStock = {}\nTgl Exp = {}\nHarga = {}\nLokasi Obat = {}"
                      .format(inv.id, inv.idObat, inv.stockObat, inv.expObat, inv.hargaObat, inv.lokasi))
        except Exception as e:
            print("===>", e)

# InventarisObat.showInventarisObat()