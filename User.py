from HakAkses import HakAkses

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

    def verifyUser(self, username, password) -> bool:
        pass

# admin = User("admin","admin",HakAkses(1))
# print(admin.hakAkses)