from sqlalchemy import Column, Integer, ForeignKey, Date
from Database.base import Base
from sqlalchemy.orm import relationship


class ResepOrm(Base):
    __tablename__ = 'resep'

    id = Column(Integer, primary_key=True)
    idDokter = Column(Integer, ForeignKey('Dokter.id'))
    idPasien = Column(Integer, ForeignKey('Pasien.id'))
    idObat = Column(Integer, ForeignKey('obat.id'))
    tglResep = Column(Date)
    # dokter = relationship("DokterOrm", back_populates="reseps")
    # pasien = relationship("PasienOrm", back_populates="reseps")
    # obat = relationship("ObatOrm", back_populates="reseps")
    # resep = relationship("TransaksiOrm", back_populates="resep")


    def __init__(self, dokter, pasien, obat, tglResep):
        self.dokter = dokter
        self.pasien = pasien
        self.obat = obat
        self.tglResep = tglResep