from sqlalchemy import Column, ForeignKey, Integer, Date
from Class.JenisObat import JenisObat
from Database.base import Base, sessionFactory
from sqlalchemy.orm import relationship

'''
This Class need Improvement on Relationship SqlAlchemy
Still confused on building relationship in sqlAlchemy
'''


class TransaksiOrm(Base):
    __tablename__ = 'transaksi'

    id = Column(Integer, primary_key=True)
    tglTransaksi = Column(Date)
    besarTransaksi = Column(Integer)
    idResep = Column(Integer, ForeignKey('resep.id'))

    def __init__(self, tglTransaksi, besarTransaksi, resep):
        self.tglTransaksi = tglTransaksi
        self.besarTransaksi = besarTransaksi
        self.idResep = resep

    @staticmethod
    def showTransaksi():
        try:
            session = sessionFactory()
            for transaksi in session.query(TransaksiOrm).all():
                print("Id Obat = {}\nTgl Transaksi = {}\nBesar Transaksi = {}\n"
                      "Id Resep = {}\n==============".format(transaksi.id, transaksi.tglTransaksi,
                                                             transaksi.besarTransaksi, transaksi.idResep))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertTransaksi(Transaksi, idResep):
        try:
            session = sessionFactory()
            transaksiOrm = TransaksiOrm(Transaksi.tglTransaksi, Transaksi.besarTransaksi, idResep)
            session.add(transaksiOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")
