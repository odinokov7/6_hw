class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_speed(self):
        print('Скорость автомобиля:', self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Автомобиль превышает допустимую скорость!')
        else:
            print('Скорость автомобиля:', self.speed)

    pass


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Автомобиль превышает допустимую скорость!')
        else:
            print('Скорость автомобиля:', self.speed)

    pass


class PoliceCar(Car):
    pass


a = PoliceCar(40, 'Желтая', 'Audi', True)
b = TownCar(62, 'Зеленая', 'Benz', False)
c = TownCar(41, 'Зеленая', 'Benz', False)
a.show_speed()
a.go()
a.turn('налево')
b.show_speed()
c.show_speed()
print(c.name)
print(b.color)
