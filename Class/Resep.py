from Dokter import Dokter
from Pasien import Pasien
from Obat import Obat

class Resep:

    def __init__(self, Dokter, Pasien, Obat = []):
         self.Dokter = Dokter
         self.Pasien = Pasien
         self.Obat = Obat


