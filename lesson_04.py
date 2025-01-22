class OrcRace:
    battle_cry = "Za hordę!"

    def __init__(self, damage, health, cost):
        self.damage = damage
        self.health = health
        self.cost_of_production = cost

    def attack(self):
        print(OrcRace.battle_cry)
        print(f"Zadałeś {self.damage} obrażeń!")

    def go_to(self, x, y):
        print(f"Idziesz do współrzędnych: {x}, {y}")