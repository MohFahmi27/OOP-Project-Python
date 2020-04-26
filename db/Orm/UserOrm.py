from sqlalchemy import Column, String, Integer
from db.base import Base, sessionFactory
from Class.HakAkses import HakAkses

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

    def deleteUser(self):
        pass

# session = sessionFactory()
# for i in session.query(UserOrm).order_by(UserOrm.id):
#     print(i.username, i.password, i.hak_akses)