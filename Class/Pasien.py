from Class.JenisKelamin import JenisKelamin
from Class.Person import Person
from Database.Orm.PasienOrm import PasienOrm
from Database.base import sessionFactory


class Pasien(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, tglLahir, noKK, noKtp):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
        self.__tglLahir = tglLahir
        self.__noKK = noKK
        self.__noKtp = noKtp

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
    def tglLahir(self):
        return self.__tglLahir

    @tglLahir.setter
    def tglLahir(self, date):
        self.__tglLahir = date

    @property
    def noKK(self):
        return self.__noKK

    @noKK.setter
    def noKK(self, noKK):
        self.__noKK = noKK

    @property
    def noKtp(self):
        return self.__noKtp

    @noKtp.setter
    def noKtp(self, noKtp):
        self.__noKtp = noKtp

    def cetakKartu(self) -> bool:
        pass

    def __str__(self):
        return "Nama Pasien : {} \nAlamat Pasien : {} \nJenis Kelamin : {} \nNo Telp : {} \nNo KK: {} \nNo KTP : {}".format(
            self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__noKK, self.__noKtp)

# pasien = Pasien("Spyan", "Di Langit Ke 2", JenisKelamin.LAKI_LAKI, "08123123", "12312313", "123123123")
# print(pasien)
# pasien.insertPasien()
# Pasien.showPasien()
