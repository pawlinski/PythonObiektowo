class SomeList:
    def __init__(self):
        self._some_list = [] # tworzy obiekt, który jest pustą listą

    def add_element(self, element):
        self._some_list.append(element) # dodaje element do listy

    # def remove_element(self, element):
    #     self._some_list.remove(element) # usuwa element z listy

    def remove_element(self):
        self._some_list.pop() # usuwa ostatni element z listy

    # def length(self):
    #     return len(self._some_list)

    def __len__(self): # przekazuje obiekt tej klasy do funkcji __len__
        return len(self._some_list)

def main():
    # print(len('Ala ma kota.'))
    # print('Ala ma kota.'.__len__()) # to samo co wyżej (metoda specjalna len dla obiektu string)

    some_list = SomeList()
    some_list.add_element(1)
    some_list.add_element(6)
    some_list.add_element(4)

    print(len(some_list))
    print(some_list.__len__())

main()