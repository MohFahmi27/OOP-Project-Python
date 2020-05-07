from sqlalchemy import Column, String, Integer, Text, Enum
from Class.JenisKelamin import JenisKelamin
from Database.base import Base, sessionFactory

'''
This Class could implement inheritance PersonOrm soon!. 
using the inheritance feature in sqlAlchemy
'''


class PasienOrm(Base):
    __tablename__ = 'Pasien'

    id = Column(Integer, primary_key=True)
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

    @staticmethod
    def showPasien():
        try:
            session = sessionFactory()
            for pasien in session.query(PasienOrm).all():
                print(
                    "Id Pasien = {}\nNama = {}\nAlamat = {}\nJenis Kelamin= {}\nNo Telp = {}\nNo KK = {}\nNo KTP = {}\n===================="
                        .format(pasien.id, pasien.namaPasien, pasien.alamatPasien, pasien.jenisKelamin,
                                pasien.noTelpPasien, pasien.noKk, pasien.noKtp))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertPasien(pasien):
        try:
            session = sessionFactory()
            pasienOrm = PasienOrm(pasien.nama, pasien.alamat, pasien.jenisKelamin,
                                  pasien.noTelp, pasien.noKK, pasien.noKtp)
            session.add(pasienOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updatePasien(idPasien):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newalamat = input("Masukkan Alamat Baru: ")
            newjenisKelamin = input("Masukkan Jenis Kelamin Baru: ")
            newNoTelp = input("Masukkan No Telp Baru: ")
            newnoKk = input("Masukkkan noKK Baru")
            newNoKtp = input("Masukkan No KTP")
            session = sessionFactory()
            session.query(PasienOrm).filter_by(id=idPasien).update({
                PasienOrm.namaPasien: newNama, PasienOrm.alamatPasien: newalamat,
                PasienOrm.jenisKelamin: newjenisKelamin, PasienOrm.noTelpPasien: newNoTelp, PasienOrm.noKk: newnoKk,
                PasienOrm.noKtp: newNoKtp
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deletePasien(idPasien):
        try:
            session = sessionFactory()
            session.query(PasienOrm).filter_by(id=idPasien).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")
