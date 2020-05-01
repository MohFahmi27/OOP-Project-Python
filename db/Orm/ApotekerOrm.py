from sqlalchemy import Column, String, Integer, Text, Enum
from Class.JenisKelamin import JenisKelamin
from db.base import Base, sessionFactory


class ApotekerOrm(Base):
    __tablename__ = 'Apoteker'

    id = Column(Integer, primary_key=True)
    namaApeteker = Column(String)
    alamatApoteker = Column(Text)
    jenisKelamin = Column(Enum(JenisKelamin))
    noTelpApoteker = Column(String)
    NIP = Column(String)

    def __init__(self, nama, alamat, jenisKelamin, noTelp, spesialis):
        self.namaApoteker = nama
        self.alamatApoteker = alamat
        self.jenisKelamin = jenisKelamin
        self.noTelpApoteker = noTelp
        self.NIP = spesialis

    @staticmethod
    def showApoteker():
        try:
            session = sessionFactory()
            for apoteker in session.query(ApotekerOrm).all():
                print(
                    "Id Apoteker = {}\nNama = {}\nAlamat = {}\nJenis Kelamin= {}\nNo Telp = {}\nNIP = {}\n===================="
                        .format(apoteker.id, apoteker.namaApoteker, apoteker.alamatApoteker, apoteker.jenisKelamin,
                                apoteker.noTelpApoteker, apoteker.NIP))
            session.close()
        except Exception as e:
            print("===>", e)

    def insertDokter(self):
        try:
            session = sessionFactory()
            apotekerOrm = ApotekerOrm(self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__nip)
            session.add(apotekerOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateApoteker(idApoteker):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newalamat = input("Masukkan Alamat Baru: ")
            newjenisKelamin = input("Masukkan Jenis Kelamin Baru: ")
            newNoTelp = input("Masukkan No Telp Baru: ")
            newnip = input("Masukkkan Spesialis Baru")
            session = sessionFactory()
            session.query(ApotekerOrm).filter_by(id=idApoteker).update({
                ApotekerOrm.namaDokter: newNama, ApotekerOrm.alamatDokter: newalamat,
                ApotekerOrm.jenisKelamin: newjenisKelamin, ApotekerOrm.noTelpApoteker: newNoTelp,
                ApotekerOrm.NIP: newnip
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteDokter(idApoteker):
        try:
            session = sessionFactory()
            session.query(ApotekerOrm).filter_by(id=idApoteker).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")
