class BankHisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.__balans = balans

    def balansni_kor(self):
        return f"{self . egasi} ning balansi : {self . __balans} so ’m"

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
            return f"{miqdor} so ’m qo ’shildi."
        return " Xato : Miqdor musbat bo’lishi kerak!"


hisob = BankHisob("Olim", 1000000)
print(hisob.balansni_kor())
print(hisob.pul_qosh(500000))
print(hisob.balansni_kor())


from abc import ABC, abstractmethod

class Shakl(ABC):
    @abstractmethod
    def yuza(self):
        pass

class Aylana(Shakl):
    def __init__(self, radius):
        self . radius = radius

    def yuza(self):
        return 3.14 * self . radius ** 2

class Tortburchak(Shakl):
    def __init__(self, eni, boyi):
        self . eni = eni
        self . boyi = boyi

    def yuza(self):
        return self.eni * self.boyi


aylana = Aylana(5)
tortburchak = Tortburchak(4, 6)
print(aylana.yuza())
print(tortburchak.yuza())
