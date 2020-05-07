from enum import Enum

class JalurEn(Enum):
    DEBIT = 1
    CASH = 2

class PenjaminanPribadi():
    def __init__(self, JalurEn):
        self.jalur = JalurEn


# pp = PenjaminanPribadi(JalurEn(2))
# print(pp.jalur)