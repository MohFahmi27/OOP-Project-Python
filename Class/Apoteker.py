from Class.Person import Person
from db.Orm.ApotekerOrm import ApotekerOrm
from db.base import sessionFactory


class Apoteker(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, nip):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
        self.__nip = nip

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat

    @property
    def jenisKelamin(self):
        return self.__jenisKelamin

    @jenisKelamin.setter
    def jenisKelamin(self, jenisKelamin):
        self.__jenisKelamin = jenisKelamin

    @property
    def noTelp(self):
        return self.__noTelp

    @noTelp.setter
    def noTelp(self, noTelp):
        self.__noTelp = noTelp

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, nip):
        self.__nip = nip

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

    @staticmethod
    def updateDokter(idDokter):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newalamat = input("Masukkan Alamat Baru: ")
            newjenisKelamin = input("Masukkan Jenis Kelamin Baru: ")
            newNoTelp = input("Masukkan No Telp Baru: ")
            newnip = input("Masukkkan Spesialis Baru")
            session = sessionFactory()
            session.query(ApotekerOrm).filter_by(id=idDokter).update({
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
    def showDokter():
        try:
            session = sessionFactory()
            for apoteker in session.query(ApotekerOrm).all():
                print(
                    "Id Pasien = {}\nNama = {}\nAlamat = {}\nJenis Kelamin= {}\nNo Telp = {}\nSpesialis = {}\n===================="
                        .format(apoteker.id, apoteker.namaApoteker, apoteker.alamatApoteker, apoteker.jenisKelamin,
                                apoteker.noTelpApoteker, apoteker.NIP))
            session.close()
        except Exception as e:
            print("===>", e)

    def laporanObatnAlkes(self, date):
        pass
