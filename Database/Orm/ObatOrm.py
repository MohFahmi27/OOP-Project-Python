from sqlalchemy import Column, String, Integer, Enum
from Class.JenisObat import JenisObat
from Database.base import Base, sessionFactory
from sqlalchemy.orm import relationship


class ObatOrm(Base):
    __tablename__ = 'obat'

    id = Column(Integer, primary_key=True)
    jenisObat = Column(Enum(JenisObat))
    namaObat = Column(String)
    # inventaris_obat = relationship("InventarisObatOrm", back_populates="obat")
    # reseps = relationship("ResepOrm", back_populates="obat")

    def __init__(self, jenisObat, namaObat):
        self.jenisObat = jenisObat
        self.namaObat = namaObat

    @staticmethod
    def showObat():
        try:
            session = sessionFactory()
            for obat in session.query(ObatOrm).all():
                print("Id Obat = {}\nJenis Obat = {}\nNama Obat = {}\n==============".format(obat.id, obat.jenisObat,
                                                                                             obat.namaObat))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertObat(obat):
        try:
            session = sessionFactory()
            obatOrm = ObatOrm(obat.jenisObat, obat.namaObat)
            session.add(obatOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateObat(idObat):
        try:
            newJenisObat = input("Masukkan jenis Obat Baru: ")
            newnamaObat = input("Masukkan nama Obat Baru: ")
            session = sessionFactory()
            session.query(ObatOrm).filter_by(id=idObat).update({
                ObatOrm.jenisObat: newJenisObat, ObatOrm.namaObat: newnamaObat
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteObat(idObat):
        try:
            session = sessionFactory()
            session.query(ObatOrm).filter_by(id=idObat).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")
