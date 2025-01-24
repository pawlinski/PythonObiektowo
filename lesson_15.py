# MRO - dziedziczenie wielokrotne
class A:
    def which_class(self):
        print('A')

class B(A):
    def which_class(self):
        print('B')

class C(B, A):
    def which_class(self):
        super().which_class() # wywoła metodę z klasy B bo jest następna w kolejności MRO
        print('C')
        print('------------------')
        B.which_class(self) # bezpośrednie odwołanie do klasy B
        A.which_class(self) # bezpośrednie odwołanie do klasy A

def main():
    c = C()

    print(C.mro()) # kolejność przeszukiwania klas
    c.which_class()


main()