from Class.JenisObat import JenisObat
from Class.Obat import Obat
from Database.Orm.InventarisObatOrm import InventarisObatOrm
from Database.base import sessionFactory
from datetime import date, timedelta
from Class.Obat import Obat


class InventarisObat():

    def __init__(self, idObat, stockObat, hargaObat, lokasi):
        self.idobat = idObat
        self.__stockObat = stockObat
        self.__expObat = (date.today()) + timedelta(weeks=26)
        self.__hargaObat = hargaObat
        self.__lokasi = lokasi

    @property
    def stockObat(self):
        return self.__stockObat

    @stockObat.setter
    def stockObat(self, stockObat):
        self.__stockObat = stockObat

    @property
    def expObat(self):
        return self.__expObat

    @property
    def hargaObat(self):
        return self.__hargaObat

    @hargaObat.setter
    def hargaObat(self, hargaObat):
        self.__hargaObat = hargaObat

    @property
    def lokasi(self):
        return self.__lokasi

    @lokasi.setter
    def lokasi(self, lokasi):
        self.__lokasi = lokasi





# paracetamol = Obat(JenisObat.SERBUK, "PuyerWal")
# paracetamol.insertObat()
# Obat.showObat()
# inventarisObat1 = InventarisObat(2, 2, 50_000, "dirak nomor 2")
# inventarisObat1.insertInventarisObat()
# InventarisObat.showInventarisObat()