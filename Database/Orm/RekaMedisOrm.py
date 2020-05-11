from sqlalchemy import Column, Integer, Date, ForeignKey

from Database.base import Base, sessionFactory


class RekamMedisOrm(Base):
    __tablename__ = 'rekam_medis'

    id = Column(Integer, primary_key=True)
    tglRekamMedis = Column(Date)
    idPasien = Column(Integer, ForeignKey("pasien.id"))
    idPenyakit = Column(Integer, ForeignKey("penyakit.id"))
    idResep = Column(Integer, ForeignKey('resep.id'))

    def __init__(self, tglRekamMedis, idPasien, idPenyakit, idResep):
        self.tglRekamMedis = tglRekamMedis
        self.idPasien = idPasien
        self.idPenyakit = idPenyakit
        self.idResep = idResep

    @staticmethod
    def showRekamMedis():
        try:
            session = sessionFactory()
            for rekamMedis in session.query(RekamMedisOrm).all():
                print("Id Obat = {}\nTgl RekamMedis = {}\nid Pasien = {}\n"
                      "Id Penyakit = {}\nId Resep = {}"
                      "\n==============".format(rekamMedis.id, rekamMedis.tglRekamMedis,
                                                rekamMedis.idPasien, rekamMedis.idPenyakit,
                                                rekamMedis.idResep))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertRekamMedis(RekamMedis, idPasien, idPenyakit, idResep):
        try:
            session = sessionFactory()
            rekamMedis = RekamMedisOrm(RekamMedis.tglRekamMedis, idPasien, idPenyakit, idResep)
            session.add(rekamMedis)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")
