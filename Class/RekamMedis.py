class RekamMedis:

    def __init__(self, tglRekamMedis):
        self.__tglRekamMedis = tglRekamMedis

    @property
    def tglRekamMedis(self):
        return self.__tglRekamMedis

    @tglRekamMedis.setter
    def tglRekamMedis(self, tglRekamMedis):
        self.__tglRekamMedis = tglRekamMedis
