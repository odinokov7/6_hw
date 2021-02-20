class Stationery:
    title = 'Название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Принт для дочернего класса Pen')


class Pencil(Stationery):
    def draw(self):
        print('Принт для дочернего класса Pencil')


class Handle(Stationery):
    def draw(self):
        print('Принт для дочернего класса Handle')


a = Stationery()
b = Pen()
c = Pencil()
d = Handle()

a.draw()
b.draw()
c.draw()
d.draw()

print(a.title)
