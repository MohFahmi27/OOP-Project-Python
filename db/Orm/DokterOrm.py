from sqlalchemy import Column, String, Integer, Text
from db.base import Base, sessionFactory
from Class.HakAkses import HakAkses

class DokterOrm(Base):
    __tablename__ = 'Dokter'

    id = Column(Integer, primary_key = True)
    namaDokter = Column(String)
    alamatDokter = Column(Text)
    jenisKelamin = Column(String)
    noTepDokter = Column(String)
    spesialis = Column(String)

    def __init__(self, nama, alamat, jenisKelamin, noTelp, spesialis):
        self.namaDokter = nama
        self.alamatDokter = alamat
        self.jenisKelamin = jenisKelamin
        self.noTepDokter = noTelp
        self.spesialis = spesialis