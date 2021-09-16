
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus' : bonus}
    def info(self):
        print (self.name)
        print (self.surname)
        print (self.position)
        print (self._income)
class Position(Worker):

    def get_full_name(self):
        print (self.name + ' ' + self.surname)
    def get_total_income(self):
        print (self._income['wage'] + self._income['bonus'])

boss = Position ('Иван', 'Иванов', 'Босс', 100000, 75000)
rab = Position ('Петр', 'Петров', 'Раб', 10000, 2000)

boss.info()
rab.info()

boss.get_full_name()
boss.get_total_income()

rab.get_full_name()
rab.get_total_income()