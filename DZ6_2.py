class Road:

    def __init__ (self, length, width):
        self._length = length
        self._width = width
        self. weight = 25
        self. height = 5
    def mass(self):
        ans = self._length * self._width * self.weight * self.height
        print (ans)
road = Road(20, 5000)
road.mass()
