from abc import ABC, abstractmethod

# Interface
class Public_Transport(ABC): # klasa pochodna od klasy abstrakcyjnej
    def transport_people(self):
        print(f'{self.__class__.__name__} transported {self.capacity}')

    @abstractmethod # metoda abstrakcyjna musi zostać zaimplementowana w każdej klasie pochodnej
    def display_info(self):
        pass

class Tram(Public_Transport):
    def __init__(self, tram_type, capacity, tram_speed):
        self.tram_type = tram_type
        self.capacity = capacity
        self.tram_speed = tram_speed

    def display_info(self):
        msg = f'Tram type: {self.tram_type}\nCapacity: {self.capacity}\nMax Speed: {self.tram_speed}'
        print(msg)

class Bus(Public_Transport):
    def __init__(self, brand, capacity, color):
        self.brand = brand
        self.capacity = capacity
        self.color = color

    def display_info(self):
        msg = f'Brand: {self.brand}\nCapacity: {self.capacity}\nColor: {self.color}'
        print(msg)

class MercedesBenzBus(Bus):
    def __init__(self, air_conditioning, *args, **kwargs):
        self.air_conditioning = air_conditioning
        super().__init__(*args, **kwargs)
        
    def display_info(self):
        super().display_info()
        print(f'Air Conditioning: {self.air_conditioning}')

def transport_people_to_city_center(obj):
    print(f'DESTINATION: city center\n{obj.__class__.__name__} waiting for people...\n{obj.__class__.__name__} ready to go!')
    obj.transport_people()

def show_transport_specification(obj):
    print(f'SPECIFICATION:')
    obj.display_info()

def main():
    avenio_tram = Tram("Avenio", 240, 80)
    volvo_bus = Bus("Volvo", 30, "white")
    mercedes_benz_bus = MercedesBenzBus(True, "Mercedes-Benz", 40, "black")

    public_transport_array = [avenio_tram, volvo_bus, mercedes_benz_bus]

    for obj in public_transport_array:
        transport_people_to_city_center(obj)
        print()
        show_transport_specification(obj)
        print("------------------------------------")

main()