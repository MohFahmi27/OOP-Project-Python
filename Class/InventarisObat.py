from Obat import Obat

class InventarisObat():
    
    def __init__(self, Obat, stockObat, expObat, hargaObat, lokasi):
        self.obat = Obat
        self.stockObat = stockObat
        self.hargaObat = hargaObat
        self.lokasi = lokasi