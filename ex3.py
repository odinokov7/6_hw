class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        _income = {'wage': wage, 'bonus': bonus}
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self.income["wage"] + self.income["bonus"]}'


a = Position('Вася', 'Пупкин', 'Начальник начальников', 85100, 32700)
b = Position('Антон', 'Павлов', 'Инженер', 43000, 11000)
print(a.get_full_name())
print(a.get_total_income())
print(b.get_full_name())
print(b.get_total_income())
