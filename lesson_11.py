class Nauczyciel:
    def __init__(self, imie, nazwisko, liczba_uczniow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.liczba_uczniow = liczba_uczniow

    def pokaz_informacje(self):
        print(f'{self.imie} {self.nazwisko} - {self.liczba_uczniow} uczniów')

class NauczycielMatematyki(Nauczyciel):
    pass

def main():
    nauczyciel = Nauczyciel('Marek', 'Tomaszewski', 40)
    nauczyciel.pokaz_informacje()

    nauczyciel_matematyki = NauczycielMatematyki('Grzegorz', 'Nowicki', 30)
    nauczyciel_matematyki.pokaz_informacje()

main()