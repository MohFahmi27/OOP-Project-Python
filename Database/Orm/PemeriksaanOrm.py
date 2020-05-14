from sqlalchemy import Column, Integer, String, Date

from Database.Orm.DokterOrm import DokterOrm
from Database.Orm.PasienOrm import PasienOrm
from Database.base import Base, sessionFactory


class PemeriksaanOrm(Base):
    __tablename__ = 'pemeriksaan'

    id = Column(Integer, primary_key=True)
    idPasien = Column(Integer)
    idDokter = Column(Integer)
    tglPemeriksaan = Column(Date)
    status = Column(String)

    def __init__(self, idPasien, idDokter, tglPemeriksaan, status):
        self.idPasien = idPasien
        self.idDokter = idDokter
        self.tglPemeriksaan = tglPemeriksaan
        self.status = status

    @staticmethod
    def showNotif():
        try:
            session = sessionFactory()
            result = []
            for pasien, dokter, periksa in session.query(PasienOrm, DokterOrm, PemeriksaanOrm).filter(
                    PasienOrm.id == PemeriksaanOrm.idPasien,
                    DokterOrm.id == PemeriksaanOrm.idDokter, PemeriksaanOrm.status == "BELUM DIPERIKSA"):
                result.append(
                    [str(dokter.namaDokter), str(pasien.namaPasien), str(periksa.tglPemeriksaan),
                     str(periksa.status)])
            return result
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def countNotif():
        return sessionFactory().query(PemeriksaanOrm).filter_by(status = "BELUM DIPERIKSA").count()

    @staticmethod
    def insertPemeriksaan(Pemeriksaan):
        session = sessionFactory()
        pemeriksaanOrm = PemeriksaanOrm(Pemeriksaan.idPasien, Pemeriksaan.idDokter,
                                        Pemeriksaan.tanggalPemeriksaan, Pemeriksaan.status)
        session.add(pemeriksaanOrm)
        session.commit()
        session.close()
