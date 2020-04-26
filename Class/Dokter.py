from Class.Person import Person
from db.base import sessionFactory
from db.Orm.DokterOrm import DokterOrm


class Dokter(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, spesialis=[]):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
        self.__spesialis = spesialis

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
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, spesialis=[]):
        self.__spesialis = spesialis

    def insertDokter(self):
        try:
            session = sessionFactory()
            # spesialis = ",".join(self.__spesialis)
            dokterOrm = DokterOrm(self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__spesialis)
            session.add(dokterOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

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

    def __str__(self):
        return "Nama Dokter : {} \nAlamat Dokter : {} \nJenis Kelamin : {} \nNo Telp : {} \nSpesialis : {}".format(
            self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__spesialis)


# d = Dokter("Rizal", "di bumi", "laki-laki", "noTelp", "corona")
# # print(d)
# d.insertDokter()
# Dokter.deleteDokter(1)
# Dokter.showDokter()
