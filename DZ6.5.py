class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print ('Запуск отрисовки')
class Pen (Stationery):

    def draw(self):
        print (f'Запуск отрисовки {self.title} #1')

class Pencil (Stationery):

    def draw(self):
        print (f'Запуск отрисовки {self.title} #2')

class Handle (Stationery):

    def draw(self):
        print (f'Запуск отрисовки {self.title} #3')

pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Handle('маркером')

pen.draw()
pencil.draw()
handle.draw()
