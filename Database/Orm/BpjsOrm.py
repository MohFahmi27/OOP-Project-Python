from sqlalchemy import Column, String, Integer, Enum
from Class.KelasBpjs import KelasBpjs
from Database.base import Base, sessionFactory


class BpjsOrm(Base):
    __tablename__ = 'bpjs'

    kodeKartu = Column(Integer, primary_key=True)
    kelasFasilitas = Column(Enum(KelasBpjs))
    namaPeserta = Column(String)

    def __init__(self, kodeKartu, kelasFasilitas, namaPeserta):
        self.kodeKartu = kodeKartu
        self.kelasFasilitas = kelasFasilitas
        self.namaPeserta = namaPeserta

    @staticmethod
    def showPasien():
        try:
            session = sessionFactory()
            for bpjs in session.query(BpjsOrm).all():
                print(
                    "No Kartu  = {}\nKelas Fasilitas = {}\nNama Peserta = {}"
                    "\n===================="
                        .format(bpjs.kodeKartu, bpjs.kelasFasilitas, bpjs.namaPeserta))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertPasien(bpjs):
        try:
            session = sessionFactory()
            bpjsOrm = BpjsOrm(bpjs.kodeKartu, bpjs.kelasFasilitas,
                              bpjs.namaPeserta)
            session.add(bpjsOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def verifyPeserta(kodeKartu) -> bool:
        try:
            session = sessionFactory()
            if ((session.query(BpjsOrm).filter_by(kodeKartu=kodeKartu).count()) == 1):
                return True
            else:
                return False
            session.close()
        except Exception as e:
            print("===>", e)
