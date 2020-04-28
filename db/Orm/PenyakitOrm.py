from sqlalchemy import Column, String, Integer, Text
from db.base import Base

class PenyakitOrm(Base):
    __tablename__ = 'penyakit'

    id = Column(Integer, primary_key = True)
    kodePenyakit = Column(String)
    kelompokPenyakit = Column(String)
    namaPenyakit = Column(String)
    gejala = Column(Text)

    def __init__(self, kodePenyakit, kelompokPenyakit, namaPenyakit, gejala):
        self.kodePenyakit = kodePenyakit
        self.kelompokPenyakit = kelompokPenyakit
        self.namaPenyakit = namaPenyakit
        self.gejala = gejala