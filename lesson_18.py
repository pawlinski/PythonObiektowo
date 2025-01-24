# __str__(self) - metoda powinna zwracać czytelną formę obiektu (w postaci tekstowej). Nieformalny tekst dla klienta.
# __repr__(self) - metoda powinna zwracać obiekt w formie, nadającej się do utworzenia tego obiektu. Formalny tekst dla developera.

import datetime

today = datetime.datetime.now()

print(today) # wywołuje niejawnie magiczną metodę srt()
print(str(today)) # to samo co wyżej
print(repr(today))

# na podstawie tekstu zwróconego przez repr() można odtworzyć dokładnie ten sam obiekt
new_date = datetime.datetime(2025, 1, 24, 12, 43, 6, 853897)
print(new_date)