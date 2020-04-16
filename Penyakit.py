class Penyakit:

    def __init__(self, kodePenyakit, kelompokPenyakit, namaPenyakit, gejala = []):
        self.__kodePenyakit = kodePenyakit
        self.__kelompokPenyakit = kelompokPenyakit
        self.__namaPenyakit = namaPenyakit
        self.__gejala = gejala

    @property
    def kodePenyakit(self):
        return self.__kodePenyakit
    
    @kodePenyakit.setter
    def kodePenyakit(self, kodePenyakit):
        self.__kodePenyakit = kodePenyakit

    @property
    def kelompokPenyakit(self):
        return self.__kelompokPenyakit
    
    @kelompokPenyakit.setter
    def kelompokPenyakit(self, kelompokPenyakit):
        self.__kelompokPenyakit = kelompokPenyakit

    @property
    def namaPenyakit(self):
        return self.__namaPenyakit
    
    @namaPenyakit.setter
    def namaPenyakit(self, namaPenyakit):
        self.__namaPenyakit = namaPenyakit

    @property
    def gejala(self):
        return self.__gejala
    
    @gejala.setter
    def gejala(self, gejala):
        self.__gejala = gejala