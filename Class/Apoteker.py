from Class.Person import Person


class Apoteker(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, tglLahir, nip):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
        self.__tglLahir = tglLahir
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
    def tglLahir(self):
        return self.__tglLahir

    @tglLahir.setter
    def tglLahir(self, date):
        self.__tglLahir = date

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, nip):
        self.__nip = nip

    def laporanObatnAlkes(self, date):
        pass
