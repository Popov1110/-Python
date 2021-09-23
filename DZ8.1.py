class Date:

    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def date_to_int (cls, dt):
        dd, mm, yy = map(int, dt.split('-'))
        return dd, mm, yy

    @staticmethod
    def valid (dt):
        dd, mm, yy = map(int, dt.split('-'))
        if dd > 31 or dd < 1 or mm < 1 or mm > 12 or yy < 1900 or yy > 2021:
            print('Неверная дата!')
        else:
            print('Все ок!')


a = Date('11-10-1999')
print(Date.date_to_int('11-10-1999'))
Date.valid('11-10-1999')





