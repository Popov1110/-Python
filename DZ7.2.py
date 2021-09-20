from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cloth(self):
        pass

class Coat(Clothes):
    ls_coat = []
    def __init__(self, V):
        self.V = V
        Coat.ls_coat.append(self)
    @property
    def cloth(self):
        return round(self.V / 6.5 + 0.5, 2)

class Suit (Clothes):
    ls_suit = []
    def __init__(self, H):
        self.H = H
        Suit.ls_suit.append(self)
    @property
    def cloth(self):
        return 2 * self.H + 0.3

def allcloth():
    a = 0
    b = 0
    for el1 in Coat.ls_coat:
        a += el1.cloth
    for el2 in Suit.ls_suit:
        b += el2.cloth
    print (f'Всего потребуется {a+b} ткани.')
coat1 = Coat(56)
coat2 = Coat(84)
coat3 = Coat(100)
suit = Suit(180)
print(f'Для пошива пальто нужно: {coat1.cloth} ткани')
print(f'Для пошива пальто нужно: {coat2.cloth} ткани')
print(f'Для пошива пальто нужно: {coat3.cloth} ткани')
print(f'Для пошива костюма нужно: {suit.cloth} ткани')
allcloth()
