from sqlalchemy import Column, String, Integer, Text, Enum
from Class.JenisKelamin import JenisKelamin
from Database.base import Base, sessionFactory


class DokterOrm(Base):
    __tablename__ = 'Dokter'

    id = Column(Integer, primary_key=True)
    namaDokter = Column(String)
    alamatDokter = Column(Text)
    jenisKelamin = Column(Enum(JenisKelamin))
    noTepDokter = Column(String)
    spesialis = Column(String)

    def __init__(self, nama, alamat, jenisKelamin, noTelp, spesialis):
        self.namaDokter = nama
        self.alamatDokter = alamat
        self.jenisKelamin = jenisKelamin
        self.noTepDokter = noTelp
        self.spesialis = spesialis

    @staticmethod
    def showDokter():
        try:
            session = sessionFactory()
            for dokter in session.query(DokterOrm).all():
                print(
                    "Id Pasien = {}\nNama = {}\nAlamat = {}\nJenis Kelamin= {}\nNo Telp = {}\nSpesialis = {}\n===================="
                        .format(dokter.id, dokter.namaDokter, dokter.alamatDokter, dokter.jenisKelamin,
                                dokter.noTepDokter, dokter.spesialis))
            session.close()
        except Exception as e:
            print("===>", e)

    def insertDokter(self):
        try:
            session = sessionFactory()
            # spesialis = ",".join(self.__spesialis)
            dokterOrm = DokterOrm(self.nama, self.alamat, self.jenisKelamin, self.noTelp, self.spesialis)
            session.add(dokterOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateDokter(idDokter):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newalamat = input("Masukkan Alamat Baru: ")
            newjenisKelamin = input("Masukkan Jenis Kelamin Baru: ")
            newNoTelp = input("Masukkan No Telp Baru: ")
            newSpesialis = input("Masukkkan Spesialis Baru")
            session = sessionFactory()
            session.query(DokterOrm).filter_by(id=idDokter).update({
                DokterOrm.namaDokter: newNama, DokterOrm.alamatDokter: newalamat,
                DokterOrm.jenisKelamin: newjenisKelamin, DokterOrm.noTelpDokter: newNoTelp,
                DokterOrm.spesialis: newSpesialis
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteDokter(idDokter):
        try:
            session = sessionFactory()
            session.query(DokterOrm).filter_by(id=idDokter).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")
