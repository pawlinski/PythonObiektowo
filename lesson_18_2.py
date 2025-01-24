class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def __str__(self):
        return f'This is a {self.color} {self.model}.'

    def __repr__(self): # flaga !r konwertuje na tekst (doda '') zwrócony z funkcji __repr__
        return f'{self.__class__.__name__}({self.color!r} {self.model!r})'
    # jeżeli zaimplementujemy TYLKO metodę __repr__, to będzie ona automatycznie wywoływana, kiedy będziemy odwoływać się do metody __str__


def main():
    bmw_1 = Car('white', 'BMW')

    print(bmw_1) # przed stworzeniem __str__ w konsoli: <__main__.Car object at 0x009AB1C0>
    print(f'This is a {bmw_1.color} {bmw_1.model}.') # lepiej stworzyć __str__
    print(bmw_1) # po stworzeniu __str__ pokazuje to samo co linijka wyżej

    print('------------------')

    print(f'bmw_1: str() - {bmw_1}')
    print(f'bmw_1: repr() - {repr(bmw_1)}')

main()