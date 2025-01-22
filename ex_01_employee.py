class Employee:
    count = 0

    def __init__(self, name, surename, email, salary):
        self.name = name
        self.surename = surename
        self.email = email
        self.monthly_salary = salary
        Employee.count += 1 # zlicza ilość utworzonych obiektów

    # metoda oblicza i zwraca wynagrodzenie roczne pracownika
    def get_annual_salary(self):
        return self.monthly_salary * 12

    # metoda pokazuje w konsoli podstawowe informacje o pracowniku
    def show_employee_information(self):
        print(f"Pracownik: {self.name} {self.surename}, adres e-mail: {self.email}, wynagrodzenie miesięczne: {self.monthly_salary}")

def main():
    employee_01 = Employee("Maciej", "Kowalski", "m.kowalski@gmail.com", 4800)
    employee_02 = Employee("Zofia", "Mała", "z.mala@poczta.fm", 12300)
    employee_03 = Employee("Kacper", "Ruciński", "k.rut@o2.pl", 8700)

    list_of_employee = []
    list_of_employee.append(employee_01)
    list_of_employee.append(employee_02)
    list_of_employee.append(employee_03)

    for employee in list_of_employee:
        print(f"{employee.name} {employee.surename} zarabia rocznie {employee.get_annual_salary()} zł.")
        employee.show_employee_information()

    print(f"Nasza firma ma zatrudnionych {Employee.count} pracowników.")

main()