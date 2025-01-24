class MineralWater:
    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other):
        a = self.sodium == other.sodium
        b = self.calcium == other.calcium
        return a and b

def main():
    staropolanka = MineralWater(32.50, 124)
    staropolanka_2 = MineralWater(32.50, 99)
    staropolanka_3 = MineralWater(32.50, 124)

    print(f'staropolanka == staropolanka_2: {staropolanka == staropolanka_2}')
    print(f'staropolanka == staropolanka_3: {staropolanka == staropolanka_3}')

main()