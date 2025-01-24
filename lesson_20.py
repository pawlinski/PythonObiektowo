"""__call__(self[, args...]) - metoda wywoływana w momencie , gdy odwołujemy się do obiektu jak do zwykłej funkcji. Klasa ma zachowywać się jak zwykła funkcja"""
# class A:
#     def __init__(self):
#         print('__init__')
#
#     def __call__(self, *args, **kwargs): # zostanie wywołana kiedy odwołamy się do obiektu jak do funkcji
#         print('__call__')
#
# def main():
#     a = A()
#     print(callable(a)) # sprawdza czy dany obiekt może być wywołany jako funkcja
#     a() # odwołanie jak do funkcji
#
# main()

def find_fibonacci_number(number): # ciąg zaczynający się od 0 i 1 a każdy następny jest sumą dwóch poprzedzających
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return find_fibonacci_number(number-1) + find_fibonacci_number(number-2) # rekurencja, czyli odwołanie do tej samej funkcji. Wykonuje samą siebie aż do momentu kiedy zwracana jest wartość

class FibonacciNumber:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1,
        }

    def __call__(self, number):
        if number not in self.cache: # jeżeli nie ma liczby w słowniku
            self.cache[number] = self.__call__(number-1) + self.__call__(number-2) # przypisujemy nową wartość
        return self.cache[number] # jeżeli jest, to zwracamy jego wartość

    def __repr__(self):
        return f'{self.cache}'

def main():
    print(find_fibonacci_number(10)) # nie zapisuje wyniku
    fib_number = FibonacciNumber()
    print(fib_number(10)) # ten sam wynik co funkcja find_fibonacci_number, ale...
    print(fib_number) # wszystkie liczby zostały zapisane w słowniku
    print(fib_number(6)) # jeżeli wynik już jest w słowniku, to nie robione są żadne obliczenia...
    print(fib_number) # tylko zwraca jego zawartość

main()