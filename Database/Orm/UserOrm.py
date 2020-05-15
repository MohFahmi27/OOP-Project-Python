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
            result = []
            for user in session.query(UserOrm).all():
                result.append([str(user.id), str(user.username), str(user.password), str(user.hak_akses)])
            return result
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def insertUser(user):
        session = sessionFactory()
        userOrm = UserOrm(user.username, user.password, user.hakAkses)
        session.add(userOrm)
        session.commit()
        session.close()

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
