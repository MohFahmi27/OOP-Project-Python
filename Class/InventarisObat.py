from Class.JenisObat import JenisObat
from Class.Obat import Obat
from Database.Orm.InventarisObatOrm import InventarisObatOrm
from Database.base import sessionFactory
from datetime import date, timedelta
from Class.Obat import Obat


class InventarisObat():

    def __init__(self, idObat, stockObat, hargaObat, lokasi):
        self.idobat = idObat
        self.stockObat = stockObat
        self.expObat = (date.today()) + timedelta(weeks=26)
        self.hargaObat = hargaObat
        self.lokasi = lokasi

# paracetamol = Obat(JenisObat.SERBUK, "PuyerWal")
# paracetamol.insertObat()
# Obat.showObat()
# inventarisObat1 = InventarisObat(2, 2, 50_000, "dirak nomor 2")
# inventarisObat1.insertInventarisObat()
# InventarisObat.showInventarisObat()