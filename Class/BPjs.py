from Class.KelasBpjs import KelasBpjs
from Database.Orm.BpjsOrm import BpjsOrm
from Database.base import sessionFactory


class BPJS:

    def __init__(self, noKartu, kelasFasilitas, namaPeserta):
        self.__kodeKartu = noKartu
        self.__kelasFasilitas = kelasFasilitas
        self.__namaPeserta = namaPeserta

    @property
    def kodeKartu(self):
        return self.__kodeKartu

    @kodeKartu.setter
    def kodeKartu(self, kodeKartu):
        self.__kodeKartu = kodeKartu

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

# bpjs = BPJS(123, KelasBpjs.KELAS_II, "Mahmud")
# bpjs.insertPasien()
# print(BPJS.verifyPeserta(123))
