from Class.Pasien import Pasien

'''
This Class for Transaction Between Patient and Admin
in here Patient get to Pay the medicine.
'''
class Transaksi():

    def __init__(self, tglTransaksi, besarTransaksi):
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

    '''
    Need Some Research First for print PDF or CSV file
    for this function.
    Using pypdf ? (I Think)
    '''
    def cetakNota(self) -> bool:
        pass
