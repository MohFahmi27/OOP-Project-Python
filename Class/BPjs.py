from Class.KelasBpjs import KelasBpjs
from db.Orm.BpjsOrm import BpjsOrm
from db.base import sessionFactory


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

    def insertPasien(self):
        try:
            session = sessionFactory()
            bpjs = BpjsOrm(self.__kodeKartu, self.__kelasFasilitas,
                           self.__namaPeserta)
            session.add(bpjs)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def showPasien():
        try:
            session = sessionFactory()
            for bpjs in session.query(BpjsOrm).all():
                print(
                    "No Kartu  = {}\nKelas Fasilitas = {}\nNama Peserta = {}"
                    "\n===================="
                        .format(bpjs.kodeKartu, bpjs.kelasFasilitas, bpjs.namaPeserta))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def verifyPeserta(kodeKartu) -> bool:
        try:
            session = sessionFactory()
            if ((session.query(BpjsOrm).filter_by(kodeKartu=kodeKartu).count()) == 1):
                return True
            else:
                return False
            session.close()
        except Exception as e:
            print("===>", e)


# bpjs = BPJS(123, KelasBpjs.KELAS_II, "Mahmud")
# bpjs.insertPasien()
# print(BPJS.verifyPeserta(123))
