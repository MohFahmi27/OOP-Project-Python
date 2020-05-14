from datetime import date


class Pemeriksaan:
    def __init__(self, idpasien, idDokter, status):
        self.__idPasien = idpasien
        self.__idDokter = idDokter
        self.__tanggalPemeriksaan = date.today()
        self.__status = status

    @property
    def idPasien(self):
        return self.__idPasien

    @idPasien.setter
    def idPasien(self, idPasien):
        self.__idPasien = idPasien

    @property
    def idDokter(self):
        return self.__idDokter

    @idDokter.setter
    def idDokter(self, idDokter):
        self.__idDokter = idDokter

    @property
    def tanggalPemeriksaan(self):
        return self.__tanggalPemeriksaan

    @property
    def status(self):
        return self.__status
