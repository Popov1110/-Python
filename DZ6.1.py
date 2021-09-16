from time import sleep
class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}

    def running (self):
        while True: #для бесконечной работы светофора=)
            for key in TrafficLight.__color:
                print('\r', end = '')
                print(key, end = '')
                sleep(TrafficLight.__color[key])
a = TrafficLight()
a.running()
# Про продвинутое задание не понял, что проверять если порядок явно задан изначально?