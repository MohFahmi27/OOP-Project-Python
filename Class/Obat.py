from Class.JenisObat import JenisObat
from db.Orm.ObatOrm import ObatOrm
from db.base import sessionFactory


class Obat():

    def __init__(self, JenisObat, namaObat):
        self.__jenisObat = JenisObat
        self.__namaObat = namaObat

    @property
    def jenisObat(self):
        return self.__jenisObat

    @jenisObat.setter
    def jenisObat(self, JenisObat):
        self.__jenisObat = JenisObat

    @property
    def namaObat(self):
        return self.__namaObat

    @namaObat.setter
    def namaObat(self, namaObat):
        self.__namaObat = namaObat

    def insertObat(self):
        try:
            session = sessionFactory()
            obatOrm = ObatOrm(self.__jenisObat, self.__namaObat)
            session.add(obatOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

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
    def showObat():
        try:
            session = sessionFactory()
            for obat in session.query(ObatOrm).all():
                print("Id Obat = {}\nJenis Obat = {}\nNama Obat = {}\n==============".format(obat.id, obat.jenisObat,
                                                                                             obat.namaObat))
            session.close()
        except Exception as e:
            print("===>", e)


# o = Obat(JenisObat(2).name, "Panadol")
# o.insertObat()
# Obat.showObat()
