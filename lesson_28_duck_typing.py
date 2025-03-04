class Kaczka:

    def kwacz(self):
        print('kwa, kwa')

    def frun(self):
        print('Kaczka lata')

class Czlowiek:

    def kwacz(self):
        print('Człowiek naśladujący kaczkę: kwa kwa')

    def frun(self):
        print('Człowiek nie lata')

kaczka = Kaczka()
czlowiek = Czlowiek()

lista_obiektow = [czlowiek, kaczka]

# for obiekt in lista_obiektow:
#     if hasattr(obiekt, 'kwacz'):
#         obiekt.kwacz()
#     if hasattr(obiekt, 'frun'):
#         obiekt.frun()

# ten sam efekt co wyżej
# for obiekt in lista_obiektow:
#     obiekt.kwacz()
#     obiekt.frun()

# co jeżeli nie ma takiego atrybutu?
for obiekt in lista_obiektow:
    try:
        obiekt.kwacz()
        obiekt.frun()
        obiekt.skacz()
    except AttributeError as exc:
        print(f'Brak atrybutu: {exc}')
