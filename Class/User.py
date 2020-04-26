from Class.HakAkses import HakAkses
from db.Orm.UserOrm import UserOrm
from db.base import sessionFactory

class User:

    def __init__(self, username, password, HakAkses):
        self.__username = username
        self.__password = password
        self.__hakAkses = HakAkses

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def hakAkses(self):
        return self.__hakAkses

    @hakAkses.setter
    def hakAkses(self, HakAkses):
        self.__hakAkses = HakAkses

    def insertUser(self):
        try:
            session = sessionFactory()
            userOrm = UserOrm(self.__username, self.__password, self.__hakAkses)
            session.add(userOrm)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def showUser():
        try:
            session = sessionFactory()
            for user in session.query(UserOrm).all():
                print("Id User = {}, Username = {}, Password = {}, Hak Akses = {}".format(user.id, user.username, user.password, user.hak_akses))
        except Exception as e:
            print(e)

    def verifyUser(self, username, password) -> bool:
        pass

# admin = User("admin2","admin",HakAkses(1).name)
# admin.insertUser()
User.showUser()