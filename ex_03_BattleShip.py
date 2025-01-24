class Ship:
    def __init__(self, damage):
        self.damage = damage

    def deal_damage(self): # pokaże nazwę klasy, która uruchomiła tę metodę oraz ilość damage
        # zamiast type() można użyć self.__class__.__name__
        print(f'Ilość zadanych obrażeń przez klasę {type(self).__name__} wynosi: {self.damage}')

class BattleShip(Ship):
    # *args - do funkcji możemy dodać nieograniczoną liczbę argumentów
    # **kwargs - funkcja może przyjmować dowolną ilość argumentów nazwanych, czyli KLUCZ: WARTOŚĆ
    def __init__(self, special_damage, *args, **kwargs): # kolejność jest ważna
        super().__init__(*args, **kwargs) # dzięki takiemu zapisowi nie martwimy się jakie argumenty zaciągnąć z klasy bazowej. Ułatwia to modyfikację tylko klasy bazowej, a reszta jest zaciągana automatycznie
        self.special_damage = special_damage
    # def __init__(self, damage, special_damage):
    #     super().__init__(damage)
    #     self.special_damage = special_damage

    def deal_special_damage(self): # pokaże nazwę klasy, która uruchomiła tę metodę oraz ilość special_damage
        print(f'Ilość zadanych obrażeń przez klasę {type(self).__name__} wynosi: {self.special_damage}')

class BigBattleShip(BattleShip):
    def __init__(self, bomb_damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bomb_damage = bomb_damage
    # def __init__(self, damage, special_damage, bomb_damage):
    #     super().__init__(damage, special_damage)
    #     self.bomb_damage = bomb_damage

    def deal_special_damage(self):
        super().deal_special_damage()

    def deal_special_damege_twice(self): # wywoła dwukrotnie metodę deal_special_damage
        for i in range(2):
            self.deal_special_damage()

    def use_bomb(self): # pokaże ilość obrażeń zgodnie z bomb_damage
        print(f'Ilość zadanych obrażeń przez klasę {type(self).__name__} używając bomb wynosi: {self.bomb_damage}')

class CargoShip(Ship):
    def __init__(self, capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = capacity
    # def __init__(self, damage, capacity):
    #     super().__init__(damage)
    #     self.capacity = capacity

    def transport(self): # ilość przetransportowanego ładunku z atrybutu capacity
        print(f'Klasa {type(self).__name__} przetransportowała {self.capacity} jednostek ładunku.')

def main():
    ship = Ship(20)
    # battle_ship = BattleShip(45, 66)
    battle_ship = BattleShip(special_damage=66, damage=45) # klucz=wartość
    # big_battle_ship = BigBattleShip(33, 56, 77)
    big_battle_ship = BigBattleShip(bomb_damage=77, special_damage=56, damage=33)
    # cargo_ship = CargoShip(10, 1200)
    cargo_ship = CargoShip(capacity=1200, damage=10)

    ship.deal_damage()
    battle_ship.deal_special_damage()
    big_battle_ship.deal_special_damege_twice()
    big_battle_ship.use_bomb()
    cargo_ship.transport()

main()