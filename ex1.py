from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        it = cycle(self.__color)
        tm = cycle([7, 2, 1])
        while True:
            print(next(it))
            sleep(next(tm))


a = TrafficLight()
a.running()
