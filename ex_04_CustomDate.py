from datetime import datetime

class CustomDate:
    def __init__(self, day, month, year):
        self.date_validation(day, month, year) # używam metody statycznej jeszcze przed stworzeniem obiektu

        self.day = day
        self.month = month
        self.year = year
        # if not datetime.date(self.year, self.month, self.day):
        #     raise ValueError('Not valid date!')

    def __repr__(self):
        if self.day < 10:
            self.day = '0'+str(self.day)
        if self.month < 10:
            self.month = '0'+str(self.month)
        return f'{self.day}-{self.month}-{self.year}'

    @classmethod
    def from_text(cls, text): # "dzień-miesiąc-rok"
        day, month, year = text.split('-')
        return cls(int(day), int(month), int(year))

    @classmethod
    def from_text_file(cls, file):
        objects_array = [] # tworzymy listę, do której będziemy dodawać kolejne obiekty
        with open(file, "r") as text_file: # otwieramy plik do odczytu (plik automatycznie się zamknie po odczycie)
            text_data = text_file.read().splitlines() #usuwamy znaki "new line"
        for date in text_data: # iterujemy po dacie
            date_object = cls.from_text(date) # tworzymy obiekt klasy CustomDate i przekazujemy do jego metody date
            objects_array.append(date_object) # dodajemy obiekt do listy
        return objects_array # zwracamy listę obiektów

    @staticmethod # nie korzysta z atrybutów klasy ani instancji
    def date_validation(day, month, year): # validacja poprawności formatu daty
        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError('Not valid date! Hator, Hator!')

def main():
    print(CustomDate(17, 4, 1979))
    print(CustomDate(7, 4, 1979))
    print('----------------------------')
    print(CustomDate.from_text("17-4-1979"))
    print('-----------FROM TEXT FILE-----------------')
    array_of_date = CustomDate.from_text_file("ex_04_text_file.txt")
    for date in array_of_date:
        print(date)
    # print('-----------TEST VALIDATION-----------------')
    # print(CustomDate(21, 55, 2021))

main()
