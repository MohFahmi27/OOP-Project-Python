from sqlalchemy import Column, String, Integer, Text
from db.base import Base, sessionFactory
from Class.HakAkses import HakAkses


class ApotekerOrm(Base):
    __tablename__ = 'Apoteker'

    id = Column(Integer, primary_key=True)
    namaApeteker = Column(String)
    alamatApoteker = Column(Text)
    jenisKelamin = Column(String)
    noTelpApoteker = Column(String)
    NIP = Column(String)

    def __init__(self, nama, alamat, jenisKelamin, noTelp, spesialis):
        self.namaApoteker = nama
        self.alamatApoteker = alamat
        self.jenisKelamin = jenisKelamin
        self.noTelpApoteker = noTelp
        self.NIP = spesialis
