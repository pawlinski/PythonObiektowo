from abc import ABC, abstractmethod

class SpaceShip(ABC): # tworzymy "interfejs", clasa abstrakcyjna

    @abstractmethod # zamiana na metode abstrakcyjną
    def attack(self):
        pass # zaznaczamy, że ta metoda musi być zaimplementowana w każdej klasie pochodnej

    def search_for_target(self): # ta metoda nie musi być nadpisywana bo nie jest m. abstrakcyjną
        print("Searching for a target...")

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
    dmg = 50

    # def magic_attack(self):
    def attack(self):  # nadpisujemy metodę z klasy "interfejs"
        print(f'Tank damage: {self.dmg} dmg.')


light_ship = LightSpaceShip()
heavy_ship = HeavySpaceShip()
magic_ship = MagicSpaceShip()
tank_ship = TankSpaceShip()
# space_shipppp = SpaceShip() # nie można stworzyć obiektu na podstawie klasy abstrakcyjnej

space_ships_array = [light_ship, heavy_ship, magic_ship, tank_ship]

# wywołuję metodę ataku dla każdego obiektu znajdującego się w liście
for space_ship in space_ships_array:
    space_ship.attack()
    space_ship.search_for_target()
    print("---------")
