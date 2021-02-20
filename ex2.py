class Road:
    def __init__(self, _lenght, _widht):
        self.lenght = _lenght
        self.widht = _widht

    def calc_asph(self):
        mass_asph_for_m = 25
        thickness = 10
        mass = self.widht * self.lenght * mass_asph_for_m * thickness
        return f'Необходимая масса {mass / 1000} тонн'


a = Road(30, 6000)
print(a.calc_asph())
