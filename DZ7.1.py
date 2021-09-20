class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.lst]))

    def __add__(self, other):
        for i in range(len(self.lst)):
            for j in range(len(other.lst[i])):
                self.lst[i][j] = self.lst[i][j] + other.lst[i][j]
        return Matrix.__str__(self)


a = Matrix ([[1,2,9], [3,4,8], [1,1,1]])
b = Matrix ([[9,8,1], [7,6,2], [9,9,9]])
print (a+b)