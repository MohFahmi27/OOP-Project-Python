from sqlalchemy import Column, String, Integer, Enum
from Class.JenisObat import JenisObat
from db.base import Base
from sqlalchemy.orm import relationship

class ObatOrm(Base):
    __tablename__ = 'obat'

    id = Column(Integer, primary_key = True)
    jenisObat = Column(Enum(JenisObat))
    namaObat = Column(String)
    inventaris_obat = relationship("InventarisObatOrm", uselist=False, backref="obat")

    def __init__(self, jenisObat, namaObat):
        self.jenisObat = jenisObat
        self.namaObat = namaObat