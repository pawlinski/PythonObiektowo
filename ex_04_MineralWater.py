class MineralWater:
    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other): # sprawdza, czy obiekty są równe
        a = self.sodium == other.sodium
        b = self.calcium == other.calcium
        return a and b
        # return (self.sodium == other.sodium and self.calcium == other.calcium)

    def __ne__(self, other): # sprawdza, czy obiekty są różne (wykorzystuje __eq__)
        return not self == other

    def __le__(self, other): # sprawdza, czy wartości atrybutów w obiekcie 1 są mniejsze równe niż w obiekcie 2
        return self.sodium <= other.sodium and self.calcium <= other.calcium

    def __lt__(self, other): # sprawdza, czy wartości atrybutów w obiekcie 1 są mniejsz niżw obiekcie 2
        return self <= other and not self == other # wykorzystuje __le__ i __eq__

    def __gt__(self, other): # sprawdza, czy obiekt 1 jest większy niż obiekt 2
        return not self <= other # wykorzystuje __le__

    def __ge__(self, other): # sprawdza czy obiekt 1 jest większy lub równy niż obiekt 2
        return not self < other # wykorzystuje __lt__

def main():
    staropolanka = MineralWater(32.50, 124)
    staropolanka_2 = MineralWater(32.50, 99)
    staropolanka_3 = MineralWater(32.50, 124)

    print(f'staropolanka == staropolanka_2: {staropolanka == staropolanka_2}')
    print(f'staropolanka == staropolanka_3: {staropolanka == staropolanka_3}')

    print('-------------------')
    print(f'staropolanka != staropolanka_2: {staropolanka != staropolanka_2}')
    print(f'staropolanka != staropolanka_3: {staropolanka != staropolanka_3}')

    print('-------------------')
    print(f'staropolanka <= staropolanka_2: {staropolanka <= staropolanka_2}')
    print(f'staropolanka < staropolanka_3: {staropolanka < staropolanka_3}')

    print('-------------------')
    print(f'staropolanka >= staropolanka_2: {staropolanka >= staropolanka_2}')
    print(f'staropolanka > staropolanka_3: {staropolanka > staropolanka_3}')

main()