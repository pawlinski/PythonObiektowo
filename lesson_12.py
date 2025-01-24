class OrcRace:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        print(f'{self.name} zadał {self.damage} obrażeń.')

class Troll(OrcRace):
    def __init__(self, name, damage, health):
        super().__init__(name, damage, health)

    def throw_spear(self):
        print('Rzut włócznią!')
        super().attack()

class Tauren(OrcRace):
    def __init__(self, name, damage, health, special_totem=False):
        super().__init__(name, damage, health)
        self.special_totem = special_totem

    def use_totem(self):
        print('Uderzenie totemem!')
        super().attack()
        if self.special_totem:
            print('Użyłeś specjalnego totemu. Dodatkowo zadałeś 20 obrażeń!')

def main():
    orc = OrcRace('Orc', 15, 10)
    troll = Troll('Troll', 20, 15)
    tauren = Tauren('Tauren', 30, 25, True)

    tauren.use_totem()
    tauren.attack()

    print(isinstance(tauren, OrcRace)) # sprawdza czy obiekt należy do klasy
    print(isinstance(tauren, Tauren))
    print(isinstance(tauren, Troll))

    print(issubclass(Tauren, OrcRace))  # sprawdza czy klasa jest pochodną drugiej klasy
    print(issubclass(Tauren, Tauren))
    print(issubclass(Tauren, Troll))

main()