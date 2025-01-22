class BankAccount:
    def __init__(self, first_name, last_name, initial_balance):
        self.first_name = first_name
        self.last_name = last_name
        self._balance = initial_balance # ustawiamy atrybut jako prywatny
        # self.full_name = f"{self.first_name} {self.last_name}" # ustawiany raz podczas tworzenia obiektu, nie zmienia się

    @property
    def full_name(self): # getter
        return f"{self.first_name} {self.last_name}"

    @property # ustawia balance jako atrybut (getter)
    def balance(self):
        return self._balance

    @balance.setter # traktowane jako setter dla atrybutu balance
    def balance(self, value):
        if value < 0: # wprowadzamy zabezpieczenie, żeby użytkownik nie mógł wprowadzić ujemnego salda
            raise ValueError("Negative amount is not allowed")
        self._balance = value

def main():
    account_1 = BankAccount("Maciej", "Zawadzki", 300)
    # print(account_1.get_balance()) # getter - pobiera aktualne saldo
    # account_1.set_balance(-20) # setter - aktualizuje saldo
    # print(account_1.get_balance()) # ponownie pobiera aktualne saldo

    print(account_1.balance)
    account_1.balance = 50
    print(account_1.balance)

    print(account_1.first_name)
    print(account_1.full_name)
    account_1.first_name = "Jan"
    print(account_1.first_name)
    print(account_1.full_name)

main()