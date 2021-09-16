class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def info(self):
        print (f'{self.name} {self. color} {self.speed}')
    def go(self):
        print ('Машина поехала!')
    def stop(self):
        print ('Машина остановилась!')
    def turn(self, direction):
        print (f'Машина поворачивает {direction}')
    def show_speed(self):
        print (f'Текущая скорость: {self.speed} км/ч')

class TownCar (Car):
    def show_speed(self):
        print (f'Текущая скорость: {self.speed} км/ч')
        if self.speed > 60: print ('Превышение скорости!!!!!')
class SportCar (Car):
    pass
class WorkCar (Car):
    def show_speed(self):
        print (f'Текущая скорость: {self.speed} км/ч')
        if self.speed > 40: print ('Превышение скорости!!!!!')
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

town = TownCar(85, 'черный', 'Audi')
sport = SportCar (220, 'красный', 'Ferrari')
work = WorkCar (45, 'Серый', 'Kamaz')
police = PoliceCar (90, 'Камуфляж', 'Уазик')

lst = [town, sport, work, police]

for el in lst:
    el.info()
    el.go()
    el.show_speed()
    el.turn('налево, а потом направо')
    el.stop()
