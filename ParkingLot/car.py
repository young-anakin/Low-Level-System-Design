from vehicle import Vehicle
from vehicle_type import vehicleType

class Car(Vehicle):
    def __init__(self, license_plate:str):
        super().__init__(license_plate=license_plate, vehicle_type=Car)