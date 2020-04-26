from Class.Person import Person
from db.Orm.PasienOrm import PasienOrm
from db.base import sessionFactory


class Pasien(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, noKK, noKtp):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
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

    def insertPasien(self):
        try:
            session = sessionFactory()
            pasienOrm = PasienOrm(self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__noKK,
                                  self.__noKtp)
            session.add(pasienOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def deletePasien(idPasien):
        try:
            session = sessionFactory()
            session.query(PasienOrm).filter_by(id=idPasien).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")

    @staticmethod
    def updatePasien(idPasien):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newalamat = input("Masukkan Alamat Baru: ")
            newjenisKelamin = input("Masukkan Jenis Kelamin Baru: ")
            newNoTelp = input("Masukkan No Telp Baru: ")
            newnoKk = input("Masukkkan noKK Baru")
            newNoKtp = input("Masukkan No KTP")
            session = sessionFactory()
            session.query(PasienOrm).filter_by(id=idPasien).update({
                PasienOrm.namaPasien: newNama, PasienOrm.alamatPasien: newalamat,
                PasienOrm.jenisKelamin: newjenisKelamin, PasienOrm.noTelpPasien: newNoTelp, PasienOrm.noKk: newnoKk,
                PasienOrm.noKtp: newNoKtp
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def showPasien():
        try:
            session = sessionFactory()
            for pasien in session.query(PasienOrm).all():
                print(
                    "Id Pasien = {}\nNama = {}\nAlamat = {}\nJenis Kelamin= {}\nNo Telp = {}\nNo KK = {}\nNo KTP = {}\n===================="
                        .format(pasien.id, pasien.namaPasien, pasien.alamatPasien, pasien.jenisKelamin,
                                pasien.noTelpPasien, pasien.noKk, pasien.noKtp))
            session.close()
        except Exception as e:
            print("===>", e)

    def __str__(self):
        return "Nama Pasien : {} \nAlamat Pasien : {} \nJenis Kelamin : {} \nNo Telp : {} \nNo KK: {} \nNo KTP : {}".format(
            self.__nama, self.__alamat, self.__jenisKelamin, self.__noTelp, self.__noKK, self.__noKtp)

# pasien = Pasien("Spyan", "Di Langit Ke 2", "Laki-Laki", "08123123", "12312313", "123123123")
# print(pasien)
# pasien.insertPasien()
Pasien.showPasien()
