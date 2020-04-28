from db.Orm.PenyakitOrm import PenyakitOrm
from db.base import sessionFactory


class Penyakit:

    def __init__(self, kodePenyakit, kelompokPenyakit, namaPenyakit, gejala=[]):
        self.__kodePenyakit = kodePenyakit
        self.__kelompokPenyakit = kelompokPenyakit
        self.__namaPenyakit = namaPenyakit
        self.__gejala = gejala

    @property
    def kodePenyakit(self):
        return self.__kodePenyakit

    @kodePenyakit.setter
    def kodePenyakit(self, kodePenyakit):
        self.__kodePenyakit = kodePenyakit

    @property
    def kelompokPenyakit(self):
        return self.__kelompokPenyakit

    @kelompokPenyakit.setter
    def kelompokPenyakit(self, kelompokPenyakit):
        self.__kelompokPenyakit = kelompokPenyakit

    @property
    def namaPenyakit(self):
        return self.__namaPenyakit

    @namaPenyakit.setter
    def namaPenyakit(self, namaPenyakit):
        self.__namaPenyakit = namaPenyakit

    @property
    def gejala(self):
        return self.__gejala

    @gejala.setter
    def gejala(self, gejala):
        self.__gejala = gejala

    def insertPasien(self):
        try:
            session = sessionFactory()
            penyakitOrm = PenyakitOrm(self.__kodePenyakit, self.__kelompokPenyakit,
                                      self.__namaPenyakit, self.__gejala)
            session.add(penyakitOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def showPenyakit():
        try:
            session = sessionFactory()
            for penyakit in session.query(PenyakitOrm).all():
                print(
                    "Id Penyakit = {}\nKode Penyakit = {}\nKelompok Penyakit = {}"
                    "\nNama Penyakit= {}\nGejala = {}\n===================="
                        .format(penyakit.id, penyakit.kodePenyakit, penyakit.kelompokPenyakit,
                                penyakit.namaPenyakit, penyakit.gejala))
            session.close()
        except Exception as e:
            print("===>", e)
