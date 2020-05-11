from sqlalchemy import Column, String, Integer, Text
from Database.base import Base, sessionFactory


class PenyakitOrm(Base):
    __tablename__ = 'penyakit'

    id = Column(Integer, primary_key=True)
    kodePenyakit = Column(String)
    kelompokPenyakit = Column(String)
    namaPenyakit = Column(String)
    gejala = Column(Text)


    def __init__(self, kodePenyakit, kelompokPenyakit, namaPenyakit, gejala):
        self.kodePenyakit = kodePenyakit
        self.kelompokPenyakit = kelompokPenyakit
        self.namaPenyakit = namaPenyakit
        self.gejala = gejala

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

    @staticmethod
    def insertPenyakit(penyakit):
        try:
            session = sessionFactory()
            penyakitOrm = PenyakitOrm(penyakit.kodePenyakit, penyakit.kelompokPenyakit,
                                      penyakit.namaPenyakit, penyakit.gejala)
            session.add(penyakitOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")
