class BPJS:
    
    def __init__(self, noKartu, kelasFasilitas, namaPeserta):
        self.__noKartu = noKartu
        self.__kelasFasilitas = kelasFasilitas
        self.__namaPeserta = namaPeserta

    @property
    def noKartu(self):
        return self.noKartu
    
    @noKartu.setter
    def noKartu(self, noKartu):
        self.__noKartu = noKartu

    @property
    def kelasFasilitas(self):
        return self.__kelasFasilitas

    @kelasFasilitas.setter
    def kelasFasilitas(self, kelasFasilitas):
        self.__kelasFasilitas = kelasFasilitas

    @property
    def namaPeserta(self):
        return self.__namaPeserta

    @namaPeserta.setter
    def namaPeserta(self, namaPeserta):
        self.__namaPeserta = namaPeserta

    @staticmethod
    def verifyPeserta(noKartu):
        pass