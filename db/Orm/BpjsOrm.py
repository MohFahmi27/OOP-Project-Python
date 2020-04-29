from sqlalchemy import Column, String, Integer, Enum
from Class.KelasBpjs import KelasBpjs
from db.base import Base

class BpjsOrm(Base):
    __tablename__ = 'bpjs'

    kodeKartu = Column(Integer, primary_key = True)
    kelasFasilitas = Column(Enum(KelasBpjs))
    namaPeserta = Column(String)

    def __init__(self, kodeKartu, kelasFasilitas, namaPeserta):
        self.kodeKartu = kodeKartu
        self.kelasFasilitas = kelasFasilitas
        self.namaPeserta = namaPeserta

    @staticmethod
    def insertBpjs():
        pass