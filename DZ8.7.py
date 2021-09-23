class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'{self.a} + {self.b}i'
        elif self.b < 0:
            return f'{self.a} - {abs(self.b)}i'
        else:
            return f'{self.a}'
    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
try:
    print('КАЛЬКУЛЯТОР КОМПЛЕКСНЫХ ЧИСЕЛ')
    x = ComplexNumber(int(input('Введите действительную часть первого числа: ')), int(input('Введите мнимую часть первого числа: ')))
    y = ComplexNumber(int(input('Введите действительную часть второго числа: ')), int(input('Введите мнимую часть второго числа: ')))
    print (x)
    print (y)
    print (x+y)
    print (x*y)
except:
    print('Введены неверные данные!!!')
