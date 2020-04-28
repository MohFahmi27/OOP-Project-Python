from sqlalchemy import Column, String, Integer, Text, Enum
from Class.JenisKelamin import JenisKelamin
from db.base import Base

class PasienOrm(Base):
    __tablename__ = 'Pasien'

    id = Column(Integer, primary_key = True)
    namaPasien = Column(String)
    alamatPasien = Column(Text)
    jenisKelamin = Column(Enum(JenisKelamin))
    noTelpPasien = Column(String)
    noKk = Column(String)
    noKtp = Column(String)

    def __init__(self, nama, alamat, jenisKelamin, noTelp, noKk, noKtp):
        self.namaPasien = nama
        self.alamatPasien = alamat
        self.jenisKelamin = jenisKelamin
        self.noTelpPasien = noTelp
        self.noKk = noKk
        self.noKtp = noKtp