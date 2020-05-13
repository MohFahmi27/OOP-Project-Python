from sqlalchemy import Column, String, Integer, ForeignKey, Date
from Database.base import Base, sessionFactory


class InventarisObatOrm(Base):
    __tablename__ = 'inventaris_obat'

    id = Column(Integer, primary_key=True)
    idObat = Column(Integer, ForeignKey('obat.id'))
    stockObat = Column(Integer)
    expObat = Column(Date)
    hargaObat = Column(Integer)
    lokasi = Column(String)

    def __init__(self, idObat, stockObat, expObat, hargaObat, lokasi):
        self.idObat = idObat
        self.stockObat = stockObat
        self.expObat = expObat
        self.hargaObat = hargaObat
        self.lokasi = lokasi

    @staticmethod
    def showInventarisObat():
        try:
            session = sessionFactory()
            for inv in session.query(InventarisObatOrm).all():
                print("Id = {}\nId Obat = {}\nStock = {}\nTgl Exp = {}\nHarga = {}\nLokasi Obat = {}"
                      .format(inv.id, inv.idObat, inv.stockObat, inv.expObat, inv.hargaObat, inv.lokasi))
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertInvenObat(inventarisObat):
        session = sessionFactory()
        inventarisObatOrm = InventarisObatOrm(inventarisObat.idobat, inventarisObat.stockObat,
                                              inventarisObat.expObat,
                                              inventarisObat.hargaObat, inventarisObat.lokasi)
        session.add(inventarisObatOrm)
        session.commit()
        session.close()