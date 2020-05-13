from sqlalchemy import Column, String, Integer, Enum
from Database.base import Base, sessionFactory
from Class.HakAkses import HakAkses


class UserOrm(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    hak_akses = Column(Enum(HakAkses))

    def __init__(self, username, password, hak_akses):
        self.username = username
        self.password = password
        self.hak_akses = hak_akses

    @staticmethod
    def showUser():
        try:
            session = sessionFactory()
            for user in session.query(UserOrm).all():
                print("Id User = {}, Username = {}, Password = {}, Hak Akses = {}".format(user.id, user.username,
                                                                                          user.password,
                                                                                          user.hak_akses))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertUser(user):
        try:
            session = sessionFactory()
            userOrm = UserOrm(user.username, user.password, user.hakAkses)
            session.add(userOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateUserPass(idUser):
        try:
            newPassword = input("Masukkan Password Baru: ")
            session = sessionFactory()
            session.query(UserOrm).filter_by(id=idUser).update({
                UserOrm.password: newPassword
            }, synchronize_session=False)
            session.commit()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteUser(username):
        try:
            session = sessionFactory()
            session.query(UserOrm).filter_by(username=username).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")

    @staticmethod
    def verifyUser(username, password) -> bool:
        try:
            session = sessionFactory()
            if ((session.query(UserOrm).filter_by(username=username, password=password).count()) == 1):
                return True
            else:
                return False
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def findHakAkses(username):
        try:
            session = sessionFactory()
            for user in session.query(UserOrm).filter_by(username = username):
                return user.hak_akses
            session.close()
        except Exception as e:
            print("===>", e)
