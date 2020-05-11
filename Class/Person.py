from abc import ABC, abstractmethod, abstractproperty

class Person(ABC):

    @abstractproperty
    def nama(self):
        pass

    @abstractproperty
    def alamat(self):
        pass

    @abstractproperty
    def jenisKelamin(self):
        pass

    @abstractproperty
    def noTelp(self):
        pass

    @abstractproperty
    def tglLahir(self):
        pass
