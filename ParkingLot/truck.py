from vehicle_type import vehicleType
from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, license_plate:str):
        super().__init__(license_plate=license_plate, vehicle_type=Truck)