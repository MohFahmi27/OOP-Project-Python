from sqlalchemy import Column, String, Integer
from .db.base import Base, sessionFactory
from ..Class.HakAkses import HakAkses

class UserOrm(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String)
    password = Column(String)
    hak_akses = Column(String)

    def __init__(self, username, password, hak_akses):
        self.username = username
        self.password = password
        self.hak_akses = hak_akses
        
    def insertUser(self):
        try:
            session = sessionFactory()
            session.add(self.username, self.password)        
            session.commit()
            session.close()
        except Exception as e:
            print(e)
        else:
            print("Data Berhasil Disimpan!")
        
    def deleteUser(self):
        pass

admin = UserOrm("admin","admin",HakAkses(1).name)
admin.insertUser()
         
