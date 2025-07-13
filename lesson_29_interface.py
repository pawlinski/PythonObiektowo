# zjawisko polimorfizmu

class SpaceShip: # tworzymy "interfejs"
    def attack(self):
        raise NotImplementedError('Attack method must be implemented')

class LightSpaceShip(SpaceShip):
    dmg = 5

    # def light_attack(self):
    def attack(self): # nadpisujemy metodę z klasy "interfejs"
        print(f'Light damage: {self.dmg} dmg.')

class HeavySpaceShip(SpaceShip):
    dmg = 10

    # def heavy_attack(self):
    def attack(self):  # nadpisujemy metodę z klasy "interfejs"
        print(f'Heavy damage: {self.dmg} dmg.')

class MagicSpaceShip(SpaceShip):
    dmg = 15

    # def magic_attack(self):
    def attack(self):  # nadpisujemy metodę z klasy "interfejs"
        print(f'Magic damage: {self.dmg} dmg.')

class TankSpaceShip(SpaceShip):
    pass


light_ship = LightSpaceShip()
heavy_ship = HeavySpaceShip()
magic_ship = MagicSpaceShip()
tank_ship = TankSpaceShip()

space_ships_array = [light_ship, heavy_ship, magic_ship, tank_ship]

# wywołuję metodę ataku dla każdego obiektu znajdującego się w liście
# for space_ship in space_ships_array:
#     if isinstance(space_ship, LightSpaceShip):
#         space_ship.light_attack()
#     elif isinstance(space_ship, HeavySpaceShip):
#         space_ship.heavy_attack()
#     elif isinstance(space_ship, MagicSpaceShip):
#         space_ship.magic_attack()
# działa poprawnie, ale jest dość zagmatwany

# po zastosowaniu "interfejsu" nie musimy sprawdzać klasy obiektu
for space_ship in space_ships_array:
    space_ship.attack()

# wywołanie metody attack na tank_ship powoduje wystąpienie wyjątku:
# NotImplementedError: Attack method must be implemented