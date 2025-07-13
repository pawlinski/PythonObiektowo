class Vehicle:
    def transport_people(self):
        print(f'{type(self).__name__} transported {self.capacity} people.')

    def transport_people_to_city_center(self):
        print(f'DESTINATION: city center\n{type(self).__name__} waiting for people...\n{type(self).__name__} ready to go!')
        self.transport_people()

    def show_transport_specification(self):
        print(f'SPECIFICATION:')
        self.display_info()

class Tram(Vehicle):
    tram_type = 'low-floor'
    capacity = 20
    max_speed = 50

    def display_info(self):
        print(f'Tram type: {self.tram_type}\nCapacity: {self.capacity}\nMax Speed: {self.max_speed}')

class Bus(Vehicle):
    brand = 'MAN'
    capacity = 40
    color = 'Red'

    def display_info(self):
        print(f'Brand: {self.brand}\nCapacity: {self.capacity}\nColor: {self.color}')

class MercedesBenzBus(Bus):
    brand = 'Mercedes Benz'
    capacity = 45
    color = 'Black'
    air_conditioning = 'True'

    def display_info(self):
        super().display_info()
        print(f'Air Conditioning: {self.air_conditioning}')

def main():
    transporter_01 = Tram()
    transporter_02 = Bus()
    transporter_03 = MercedesBenzBus()

    transport_list = [transporter_01, transporter_02, transporter_03]

    for transporter in transport_list:
        # transporter.transport_people()
        # transporter.display_info()
        transporter.transport_people_to_city_center()
        transporter.show_transport_specification()

main()