class Cell:
    def __init__(self, pieces):
        self.pieces = int(pieces)

    def __add__(self, other):
        return self.pieces + other.pieces

    def __sub__(self, other):
        sub = self.pieces - other.pieces
        return sub if sub > 0 else 'Слишком большое вычитаемое=)'

    def __truediv__(self, other):
        return self.pieces // other.pieces

    def __mul__(self, other):
        return self.pieces * other.pieces

    def make_order(self, row):
        result = ''
        for i in range(self.pieces // row):
            result += '*' * row + '\n'
        result += '*' * (self.pieces % row) + '\n'
        return result


cell = Cell(24)
cell_2 = Cell(5)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))