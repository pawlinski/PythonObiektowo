class Library:

    def __init__(self, books=None):
        self._books = set()
        # jeżeli zostaną podane książki w argumencie, to funkcja doda je do biblioteki
        if books:
            for book in books:
                self.add_book(book)

    @property
    def number_of_books(self):
        return len(self._books)

    def add_book(self, book):
        self._books.add(book)

    def borrow_book(self, book):
        try:
            self._books.remove(book)
        except KeyError:
            print(f'Książki {book} nie ma w bibliotece.')

    def show_books(self):
        for book in self._books:
            print(book)

def main():
    libr_01 = Library()

    libr_01.add_book('Ania z Zielonego Wzgórza')
    libr_01.add_book('Gwiezdne Wojny')
    libr_01.add_book('Maroko')
    libr_01.add_book('Kubuś Puchatek')
    libr_01.add_book('Kubuś Puchatek')

    print(f'Dodałem {libr_01.number_of_books} książek do biblioteki')

    print('Chcę wypożyczyć książkę "Kajaki"')
    libr_01.borrow_book('Kajaki')
    print(f'W bibliotece są obecnie {libr_01.number_of_books} książki.')

    print('Chcę wypożyczyć książkę "Maroko"')
    libr_01.borrow_book('Maroko')
    print(f'W bibliotece są obecnie {libr_01.number_of_books} książki.')

    print('W bibliotece są następujące tytuły:')
    libr_01.show_books()

    libr_02 = Library(('PHP', 'CSS', 'C#'))
    print(f'W bibliotece 2 są obecnie {libr_02.number_of_books} książki.')

    print('W bibliotece 2 są następujące tytuły:')
    libr_02.show_books()

main()