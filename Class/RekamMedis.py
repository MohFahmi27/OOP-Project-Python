# from Pasien import Pasien
# from Penyakit import Penyakit
# from Resep import Resep
# from Dokter import Dokter
# from Obat import Obat
# from JenisObat import JenisObat

class RekamMedis():

    def __init__(self, Pasien, tglRekamMedis, Resep, Penyakit):
        self.Pasien = Pasien
        self.tglRekamMedis = tglRekamMedis
        self.Resep = Resep
        self.Penyakit = Penyakit

# p = Pasien("fjfj","fff","ff",'fff','good')
# d = Dokter("fjsssfj","ddd","dd",'ddd','ddd',['umum'])
# o = Obat(JenisObat(2), "somtehing")
# r = Resep(d, p, [o])

# rek = RekamMedis(p, d, o, r)
# print(rek.Pasien)