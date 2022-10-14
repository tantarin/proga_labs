class Car(object):
    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)
    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]
    def fuel_level(self):
        return self._tank.level
