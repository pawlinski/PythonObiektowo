import datetime

class CustomDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        if not datetime.date(self.year, self.month, self.day):
            raise ValueError('Not valid date!')

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

def main():
    print(CustomDate(17, 4, 1979))
    print(CustomDate(7, 4, 1979))
    print('----------------------------')
    print(CustomDate.from_text("17-4-1979"))
    print(CustomDate(41,5,2021))

main()
