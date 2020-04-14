from Pasien import Pasien

class Transaksi():

    def __init__(self, tglTransaksi, besarTransaksi, Pasien):
        self.__tglTransaksi = tglTransaksi
        self.__besarTransaksi = besarTransaksi
        self.Pasien = Pasien

    @property
    def tglTransaksi(self):
        return self.__tglTransaksi

    @tglTransaksi.setter
    def tglTransaksi(self, tglTransaksi):
        self.__tglTransaksi = tglTransaksi
    
    @property
    def besarTransaksi(self):
        return self.__besarTransaksi

    @besarTransaksi.setter
    def besarTransaksi(self, besarTransaksi):
        self.__besarTransaksi = besarTransaksi
