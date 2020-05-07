from sqlalchemy import Column, ForeignKey, Integer, Date
from Class.JenisObat import JenisObat
from Database.base import Base
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
    # I'm Not Sure about this one
    idPasien = Column(Integer, ForeignKey('Pasien.id'))

    def __init__(self, tglTransaksi, besarTransaksi):
        self.tglTransaksi = tglTransaksi
        self.besarTransaksi = besarTransaksi
