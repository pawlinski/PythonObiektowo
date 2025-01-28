"""Matody instancji, klasy oraz statyczne
- metody statyczne - przez parametr self mają dostęp do atrybutów instancji obiektu.
  mogą edytować stan obiektu oraz klasy.
- metody klasy (@classmethods) - poprzez parametr cls mają dostęp do atrybutów klasy.
  mogą edytować stan klasy.
- metody statyczne (@staticmethods) - nie posiadają parametru self i cls. W związku z tym
  nie mogą edytować stanu obiektu oraz klasy. Są one logicznie związane z klasą."""

class Employee:
    EMPLOYEES_GRADES = { # atrybut klasy, który jest słownikiem
        'A': '2500',
        'B': '3000',
        'C': '3500',
        'D': '4000',
    }

    # metody instancji:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        # czy grade znajduje się w słowniku
        if grade not in Employee.EMPLOYEES_GRADES:
            raise ValueError(f'Wrong employee grade. Available grades: {list(Employee.EMPLOYEES_GRADES)}')
        # tworze trzeci atrybut instancji, jeżeli istnieje
        self.grade = grade

    def show_employee_information(self):
        print(f'Name: {self.first_name} {self.last_name}, Salary: {Employee.EMPLOYEES_GRADES[self.grade]}')

    def show_grades(self): # pokazuje grade i wynagrodzenie dla danego grade
        for grade, salary in Employee.EMPLOYEES_GRADES.items():
            print(f'{grade} - {salary}')
    # w metodach instancji zamiast odwoływać się przez Employee. możemy użyć self.

    # metody klasy
    @classmethod
    def add_grade(cls, grade, salary): # nie ma dostępu do instancji = nie może korzystać z atrybutów instancji
        # metoda ta będzie dodawać do słownika kolejny grade i jego wartość (może korzystać z atrybutów klasy
        cls.EMPLOYEES_GRADES[grade] = salary # to samo Employee.EMPLOYEES_GRADES[grade] = salary

    @classmethod
    def create_from_string(cls, text): # przyjęcie tekstu i zamiana w argumenty dla konstruktora
        # metoda tworzy alternatywny konstruktor
        first_name, last_name, grade = text.split(';')
        return  cls(first_name, last_name, grade) # to samo Employee(first_name, last_name, grade)

    # metody statyczne
    @staticmethod
    def who_is_your_manager():
        # może być stworzona poza klasą, ale znajduje się w klasie, bo jest z nią powiązana logicznie
        print('The manager is Janusz Woźny.') # każdy obiekt tej klasy ma tego samego managera


def main():
    # metody instancji
    emp_1 = Employee('Agata', 'Wróbel', 'D')
    emp_1.show_employee_information()
    emp_1.show_grades()
    print('--------------------------------------\n')

    # metody klasy
    emp_1.add_grade('E','4500') # możemy odnieść się przez instancję
    Employee.add_grade('F', '5000') # lub samą klasę

    emp_1.show_grades()
    print('--------------------------------------\n')

    # emp_2 = Employee('Jan;Pokolski;C')
    # TypeError: __init__() missing 2 required positional arguments: 'last_name' and 'grade'
    emp_2 = Employee.create_from_string('Jan;Pokolski;C') # tworzymy nowy obiekt klasy Employee
    emp_2.show_employee_information()

    print('--------------------------------------\n')
    # metoda statyczna
    Employee.who_is_your_manager() # może ją wywołać klasa
    emp_2.who_is_your_manager() # jkak i instancja
main()