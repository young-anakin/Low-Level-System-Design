# This should house a specific vehicle
# a vehicle has a license number identification and also 
# it should be an abstract class because other specific vehicles will extend it
# it should also have a vehicle type
from vehicle_type import vehicleType
from abc import ABC

class Vehicle(ABC):
    def __init__(self, license_plate:str, vehicle_type:vehicleType):
        self.license_plate = license_plate
        self.type = vehicle_type
    def getType(self):
        return self.type