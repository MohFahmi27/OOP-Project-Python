from sqlalchemy import Column, String, Integer
from db.base import Base, sessionFactory
from sqlalchemy.orm import relationship
from Class.HakAkses import HakAkses

class ObatOrm(Base):
    __tablename__ = 'obat'

    id = Column(Integer, primary_key = True)
    jenisObat = Column(String)
    namaObat = Column(String)
    inventaris_obat = relationship("InventarisObatOrm", uselist=False, backref="obat")

    def __init__(self, jenisObat, namaObat):
        self.jenisObat = jenisObat
        self.namaObat = namaObat