class OrcRace:
    battle_cry = "Za hordę!"

    def __init__(self, name, damage, health, cost):
        self.name = name
        self.damage = damage
        self.health = health
        self.cost_of_production = cost

    def attack(self):
        print(OrcRace.battle_cry)
        print(f"{self.name} zadał {self.damage} obrażeń!")

    def go_to(self, x, y):
        print(f"{self.name} idzie do współrzędnych: {x}, {y}")

def main():
    orc = OrcRace("ork", 20, 20, 10)
    troll = OrcRace("troll", 25, 10, 8)
    tauren = OrcRace("tauren", 35, 40, 25)

main()