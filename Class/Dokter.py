from Class.JenisKelamin import JenisKelamin
from Class.Person import Person
from Database.base import sessionFactory
from Database.Orm.DokterOrm import DokterOrm


class Dokter(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, tglLahir, spesialis=[]):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
        self.__tglLahir = tglLahir
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
    def tglLahir(self):
        return self.__tglLahir

    @tglLahir.setter
    def tglLahir(self, date):
        self.__tglLahir = date

    @property
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, spesialis=[]):
        self.__spesialis = spesialis

    def __str__(self):
        return "Nama Dokter : {} \nAlamat Dokter : {} \nJenis Kelamin : {} \nNo Telp : {} \nSpesialis : {}".format(
            self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__spesialis)

# d = Dokter("Rizal", "di bumi", JenisKelamin.LAKI_LAKI, "noTelp", "corona")
# d.insertDokter()
# Dokter.deleteDokter(4)
# Dokter.showDokter()
