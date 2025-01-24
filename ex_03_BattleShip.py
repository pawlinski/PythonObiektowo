class Ship:
    def __init__(self, damage):
        self.damage = damage

class BattleShip(Ship):
    def __init__(self, damage, special_damage):
        super().__init__(damage)
        self.special_damage = special_damage

class BigBattleShip(BattleShip):
    def __init__(self, damage, special_damage, bomb_damage):
        super().__init__(damage, special_damage)
        self.bomb_damage = bomb_damage

class CargoShip(Ship):
    def __init__(self, damage, capacity):
        super().__init__(damage)
        self.capacity = capacity