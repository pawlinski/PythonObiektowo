class Library:

    def __init__(self, books=None):
        self.books = books = set()

    @property
    def number_of_books(self):
        return len(self.books)

    def add_book(self, book):
        self.books.add(book)

    def borrow_book(self, book):
        try:
            self.books.remove(book)
        except KeyError:
            print(f'Książki {book} nie ma w bibliotece.')

    def show_books(self):
        for book in self.books:
            print(book)

def main():
    libr_01 = Library()

    libr_01.add_book('Ania z Zielonego Wzgórza')
    libr_01.add_book('Gwiezdne Wojny')
    libr_01.add_book('Maroko')
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

main()