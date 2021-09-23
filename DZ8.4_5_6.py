class NeTuda (Exception):
    pass

class Warehouse:
    sklad = {'Принтеры' : [0,[]], 'Сканеры' : [0,[]], 'Ксероксы': [0,[]]}
    vydano = {'Бухгалтерия' : [0,[]], 'Секретариат' : [0,[]], 'Отдел продаж': [0,[]]}
    @staticmethod
    def priem (obj):
        if obj.__class__.__name__ == 'Printer':
            Warehouse.sklad['Принтеры'][0] += 1
            Warehouse.sklad['Принтеры'][1].append(obj)
        elif obj.__class__.__name__ == 'Scanner':
            Warehouse.sklad['Сканеры'][0] += 1
            Warehouse.sklad['Сканеры'][1].append(obj)
        elif obj.__class__.__name__ == 'Xerox':
            Warehouse.sklad['Ксероксы'][0] += 1
            Warehouse.sklad['Ксероксы'][1].append(obj)

    @staticmethod
    def peredacha (obj):
        try:
            otd = input('Куда передаем?')
            my_list = []
            for key in Warehouse.vydano:
                my_list.append(key)
            if otd not in my_list:
                raise NeTuda
            t = False
            for key in Warehouse.sklad:
                if obj in Warehouse.sklad[key][1]:
                    Warehouse.vydano[otd][0] += 1
                    Warehouse.vydano[otd][1].append(obj)
                    if obj.__class__.__name__ == 'Printer':
                        Warehouse.sklad['Принтеры'][0] -= 1
                        Warehouse.sklad['Принтеры'][1].remove(obj)
                        t = True
                    elif obj.__class__.__name__ == 'Scanner':
                        Warehouse.sklad['Сканеры'][0] -= 1
                        Warehouse.sklad['Сканеры'][1].remove(obj)
                        t = True
                    elif obj.__class__.__name__ == 'Xerox':
                        Warehouse.sklad['Ксероксы'][0] -= 1
                        Warehouse.sklad['Ксероксы'][1].remove(obj)
                        t = True

            if t == False:
                print ('На складе нет такой позиции, передача невозможна!!!')
        except NeTuda:
            print(f'Подразделения {otd} в компании нет!!!')

    @staticmethod
    def info_sklad ():
        print (Warehouse.sklad)

    @staticmethod
    def info_vydano():
        print(Warehouse.vydano)


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    pass

class Printer (OfficeEquipment):
    def __init__(self, brand, model, price, speed):
        super().__init__(brand, model, price)
        self.speed = speed

class Scanner (OfficeEquipment):
    def __init__(self, brand, model, price, maxformat):
        super().__init__(brand, model, price)
        self.maxformat = maxformat

class Xerox (OfficeEquipment):
    def __init__(self, brand, model, price, dpi):
        super().__init__(brand, model, price)
        self.dpi = dpi


p1 = Printer('HP', '352', 1000, 50)
p2 = Printer('Okki', 'f101', 2000, 85)
s1 = Scanner('Samsung', 's1430', 1100, 'A4')
s2 = Scanner('Samsung', 's1480', 1250, 'A3')
x1 = Xerox('Canon', 'x654', 750, 1200)

Warehouse.priem(p1)
Warehouse.priem(p2)
Warehouse.priem(s1)
Warehouse.priem(s2)

Warehouse.info_sklad()


Warehouse.peredacha(p1)
Warehouse.peredacha(s2)
Warehouse.peredacha(x1)

Warehouse.info_sklad()
Warehouse.info_vydano()